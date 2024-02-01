from flask import Flask, render_template

app = Flask(__name__, template_folder= 'templates')
app.secret_key = 'secret_key'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/base')
def base():
  return render_template('base.html')


app.run(host = "0.0.0.0",port= 8080)