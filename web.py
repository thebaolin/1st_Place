from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

def initialize_lists():
    global restaurants, choices
    restaurants = ["A", "B", "C", "D"]
    choices = []



@app.route("/")
def home():
    return render_template("index.html")

@app.route('/begin', methods=['POST'])
def begin():
    initialize_lists()
    return redirect(url_for('choose'))

@app.route("/choose", methods=['GET','POST'])
def choose():
    global restaurants, choices
    if request.method == 'GET':
        curr = restaurants[:2]
        return render_template("restaurants.html" , given = curr)
    elif request.method == 'POST':
        restaurant_choice = request.form.get("restaurant")

        choices.append(restaurant_choice)

        restaurants.pop(0)
        restaurants.pop(0)

        if restaurants:
            curr = restaurants[:2]
            return render_template("restaurants.html" , given = curr)
        elif len(choices) > 1:
            restaurants = choices
            choices = []
            return redirect(url_for('choose'))
        else:
            return redirect(url_for('result'))
        
@app.route("/result")
def result():
    return render_template("result.html", choice=choices[0])


if __name__ == "__main__":
    app.run()