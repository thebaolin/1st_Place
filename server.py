from flask import Flask, render_template, request, redirect, url_for
import requests
import config
import random
from location import Location

app = Flask(__name__)
api_key = config.API_KEY

def initialize_lists():
    global list, choices, round_num
    list = []
    choices = []
    round_num = 1

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        initialize_lists()
        input_value = request.form.get('location')
        latitude, longitude = geocode(input_value)
        data = getJSON(latitude, longitude)
        locations = data['places']
        for place in locations:
            pics = []
            for pic in place['photos'][1:]:
                pics.append(pic['name'])
            tmp = Location(place['displayName']['text'], place['formattedAddress'], place['rating'], place['userRatingCount'], place['primaryType'], f"https://places.googleapis.com/v1/{place['photos'][0]['name']}/media?maxHeightPx=400&maxWidthPx=400&key={api_key}", pics, place['priceLevel'])
            list.append(tmp)
        return redirect(url_for('choose'))

    return render_template("index.html", api_key = api_key)

@app.route('/current-location', methods = ['POST'])
def getNearBy():
    if request.method == "POST":
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        data = getJSON(latitude, longitude)
    return render_template("index.html", api_key = api_key)

def getJSON(latitude, longitude):
    URL = "https://places.googleapis.com/v1/places:searchNearby"
    payload = {
        'includedTypes' : ['japanese_restaurant'],
        'maxResultCount' : 20,
        'locationRestriction' : {
            "circle": {
                "center": {
                 "latitude": latitude,
                "longitude": longitude
            },
            "radius": 500.0
            }
        },
    }

    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': 'places.rating,places.userRatingCount,places.displayName,places.formattedAddress,places.primaryType,places.photos,places.priceLevel'
    }

    response = requests.post(URL, json=payload, headers=headers)
    print(response.json())
    return response.json()

def geocode(address):
    key = config.API_KEY
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # Extract latitude and longitude from the response
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            print(f"Geocoding failed with status: {data['status']}")
    else:
        print(f"Failed to geocode address. Status code: {response.status_code}")

@app.route("/choose", methods=['GET','POST'])
def choose():
    global list, choices, round_num
    if request.method == 'GET':
        random.shuffle(list)
        curr = list[:2]
        return render_template("restaurants.html" , given = curr , rounds = round_num)
    elif request.method == 'POST':
        restaurant_choice = request.form.get("restaurant")

        choices.append(restaurant_choice)

        list.pop(0)
        list.pop(0)

        if len(list) == 1:
            choices.append(list[0])
            list.pop(0)

        if list:
            curr = list[:2]
            return render_template("restaurants.html" , given = curr, rounds = round_num)
        elif len(choices) > 1:
            list = choices
            choices = []
            round_num += 1
            return redirect(url_for('choose'))
        else:
            return redirect(url_for('result'))

@app.route("/result")
def result():
    return render_template("result.html", choice=choices[0])

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)

    