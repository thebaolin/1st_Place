#INSTRUCTIONS TO START:
#need to install FLASK
#one terminal: python3 -m http.server
#another terminal: python3 app.py

from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)

# load restauraunt data
with open('restaurants.json', 'r') as file:
    restaurants = json.load(file)

# http://127.0.0.1:5000/pick
@app.route('/pick', methods=['GET', 'POST'])
def pick():
    if request.method == 'GET':
        # randomly select 2 diff choices
        choices = get_random_choices()
        return render_template('pick.html', choices=choices)
    
    elif request.method == 'POST':
        try:
            # get user choice from form
            user_choice = request.form['choice']
            print(f"User choice: {user_choice}")

            # do logic here, havent implemented tournament system yet

            # redirect to pick route for new set of choices
            return redirect(url_for('pick'))
        except KeyError:
            # handle the case where 'choice' key is not present in form data
            print("KeyError: 'choice' not found in form data")
            return "Invalid form submission. Please try again."


def get_random_choices():
    choices = random.sample(restaurants, 2)
    return choices

if __name__ == '__main__':
    app.run(debug=True)
