
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('name.html', name=name)

@app.route('/swdadjoke')
def swdadjoke():
    return render_template('swjokes.html')

@app.route('/farm')
def farm():
    return render_template('farm.html')