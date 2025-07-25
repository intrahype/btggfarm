
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/swdadjoke')
def swdadjoke():
    return '<h1>Why did Princess Leia change her hair on Hoth?</h1> <b> insert pause </b> <h1> She was freezing her Buns off!</h1>'

