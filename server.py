from flask import Flask, render_template, request, jsonify
import requests
import config
from location import Location

app = Flask(__name__)
api_key = config.API_KEY
list = []

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        input_value = request.form.get('location')
        latitude, longitude = geocode(input_value)
        data = getJSON(latitude, longitude)
        locations = data['places']
        for place in locations:
            pics = []
            for pic in place['photos']:
                pics.append(pic['name'])
            tmp = Location(place['displayName']['text'], place['formattedAddress'], place['rating'], place['userRatingCount'], place['primaryType'], pics)
            list.append(tmp)

    return render_template("index.html", api_key = api_key)

@app.route('/current-location', methods = ['POST'])
ef getNearBy():
    if request.method == "POST":
        selected_options = request.json.get('selectedOptions')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        data = getJSON(selected_options, latitude, longitude)
        # Process the data from the Google Places API
        return jsonify(data)
    else:
        # Return an error response if the request method is not POST
        return jsonify({'error': 'Invalid request method'})

def getJSON(latitude, longitude):
    URL = "https://places.googleapis.com/v1/places:searchNearby"
    payload = {
        'includedTypes' : selected_options,
        'maxResultCount' : 2,
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
        'X-Goog-FieldMask': 'places.rating,places.userRatingCount,places.displayName,places.formattedAddress,places.primaryType,places.photos'
    }

    response = requests.post(URL, json=payload, headers=headers)
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


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)

    