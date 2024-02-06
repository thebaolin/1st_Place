from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)
api_key = config.API_KEY

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        input_value = request.form.get('location')
        latitude, longitude = geocode(input_value)
        data = getJSON(latitude, longitude)
    return render_template("index.html", api_key = api_key)

@app.route('/current-location', methods = ['POST'])
def getNearBy():
    if request.method == "POST":
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        data = getJSON(latitude, longitude)
        return f'{latitude}, {longitude}'
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
        'X-Goog-FieldMask': 'places.displayName,places.formattedAddress,places.primaryType'
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


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)

    