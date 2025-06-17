from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World! This site will serve to track the specific mods for a coop farm at https://www.twitch.tv/narrrayu on Saturdays at 00:30 GMT 19:30 EST 16:30 PST || </h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/swdadjoke')
def swdadjoke():
    return '<h1>Why did Princess Leia change her hair on Hoth?</h1> <b> insert pause </b> <h1> She was freezing her Buns off!</h1>'

