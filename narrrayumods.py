<<<<<<< HEAD
from flask import Flask
import os.path
from flask_sqlalchemy import SQLAlchemy
=======

from flask import Flask, render_template
>>>>>>> 45aeec39730167c4fcf9a0e48db70bc00a540b3f

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
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('name.html', name=name)

@app.route('/swdadjoke')
def swdadjoke():
    return render_template('swjokes.html')

<<<<<<< HEAD
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
=======
@app.route('/farm')
def farm():
    return render_template('farm.html')
>>>>>>> 45aeec39730167c4fcf9a0e48db70bc00a540b3f
