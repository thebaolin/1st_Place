from flask import Flask, redirect, url_for, render_template, request
import random

app = Flask(__name__)

def initialize_lists():
    global restaurants, choices, round_num
    restaurants = ["A", "B", "C", "D"]
    choices = []
    round_num = 1



@app.route("/", methods=['GET' , 'POST'])
def home():
    return render_template("index.html")

@app.route('/begin', methods=['POST'])
def begin():
    initialize_lists()
    return redirect(url_for('choose'))

@app.route("/choose", methods=['GET','POST'])
def choose():
    global restaurants, choices , round_num
    if request.method == 'GET':
        random.shuffle(restaurants)
        curr = restaurants[:2]
        return render_template("restaurants.html" , given = curr , rounds = round_num)
    elif request.method == 'POST':
        restaurant_choice = request.form.get("restaurant")

        choices.append(restaurant_choice)

        restaurants.pop(0)
        restaurants.pop(0)

        if restaurants:
            curr = restaurants[:2]
            return render_template("restaurants.html" , given = curr, rounds = round_num)
        elif len(choices) > 1:
            restaurants = choices
            choices = []
            round_num += 1
            return redirect(url_for('choose'))
        else:
            return redirect(url_for('result'))
        
@app.route("/result")
def result():
    return render_template("result.html", choice=choices[0])


if __name__ == "__main__":
    app.run()