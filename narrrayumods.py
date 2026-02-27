from flask import Flask
import os.path
from flask_sqlalchemy import SQLAlchemy

# database SQLite
db = SQLAlchemy()

# start app
app = Flask(__name__)

# db name
db_name = 'mod_list.db'

# path to db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)

app.config['SQLALchemy_DATABASE_URI'] = 'sqlite:///' + db_path

app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = True

# initialize app with SQLAlchemy
db.init_app(app)

# database Class
class Mods(db.Model):
    __tablename__ = 'Stardew Valley Mods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_updated = db.Column(db.String)

@app.route('/')
def index():
    return '<h1>Hello World! This site will serve to track the specific mods for a coop farm at https://www.twitch.tv/narrrayu on Saturdays at 00:30 GMT 19:30 EST 16:30 PST || </h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/swdadjoke')
def swdadjoke():
    return '<h1>Why did Princess Leia change her hair on Hoth?</h1> <b> insert pause </b> <h1> She was freezing her Buns off!</h1>'

@app.route('/modlist')
def modlist():
    try:
        mod_list = db.session.execute(db.select(Mods))

        mod_text = '<ul>'
        for mod in mod_list:
            mod_text += '<li>' + mod_list.name + ', ' + mod_list.lastupdated + '</li>'
    
    except Exception as error:
        #user error to hold error description
        error_text = "<p>The error:<br>" + str(error) + "</p>"
        header_return = '<h1>Something has broken.</h1>'
        return header_return + error_text



if __name__ == "__main__":
    app.run(debug=True)