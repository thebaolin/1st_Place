from flask import Flask, render_template,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import SelectField
import json

with open('static/restaurant.json') as restaurant_js:
      restaurant_js_data = json.load(restaurant_js)
restaurant_info = {'data': restaurant_js_data}
  
app = Flask(__name__, template_folder= 'templates')
app.secret_key = 'secret_key'

app.context_processor(lambda: restaurant_info)

class MyForm(FlaskForm):
  options = SelectField('What do you perfer the most?', choices = [('rating','Rating'),('atmosphere','Atmosphere'),('location','Location'),('tasty','Tasty'),('price','Price')])


@app.route('/')
def index():
  form = MyForm()
  return render_template('index.html', form = form)
 
@app.route('/base', methods = ['GET','POST'])
def base():
  return render_template('base.html')

@app.route('/result', methods = ['GET','POST'])
def result():
  form  = MyForm()
  if form.validate_on_submit:
    choices = form.options.data
  if choices == 'rating':
    return redirect(url_for('base'))
  elif choices == 'atmosphere':
    return redirect(url_for('base'))
  elif choices == 'location':
    return redirect(url_for('base'))
  elif choices == 'tasty':
    return redirect(url_for('base'))
  elif choices == 'price':
    return redirect(url_for('base'))
  return render_template('submit.html',form = form)


app.run(host = "0.0.0.0", port= 8080 )
