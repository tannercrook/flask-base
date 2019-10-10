from flask import Flask 
from flask import render_template
from flask_adminlte import AdminLTE
import dateutil.parser

app = Flask(__name__)
AdminLTE(app)

class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "John Doe"
    avatar = "/static/img/user2-160x160.jpg"
    created_at = dateutil.parser.parse("November 12, 2012")

# This is a placeholder user object.  In the real-world, this would
# probably get populated via ... something.
current_user = User()

@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)

@app.route('/login')
def login():
    return render_template('login.html', current_user=current_user)

@app.route('/lockscreen')
def lockscreen():
    return render_template('lockscreen.html', current_user=current_user)