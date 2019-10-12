from flask import Flask 
from flask import render_template
from flask_adminlte import AdminLTE


# Custom class imports
from models.DBase import connection
from models.User import User

app = Flask(__name__)
AdminLTE(app)

# This is a placeholder user object.  In the real-world, this would
# probably get populated via ... something.
current_user = User()
current_user.full_name = "Tanner Crook"

@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)

@app.route('/login')
def login():
    return render_template('login.html', current_user=current_user)

@app.route('/lockscreen')
def lockscreen():
    return render_template('lockscreen.html', current_user=current_user)