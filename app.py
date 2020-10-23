from flask import Flask, render_template, session


app = Flask(__name__)
app.config['SECRET_KEY']='\xb6"\x8e\x89L\xc7\xaeJ\x80\xef\x87\xdfL\x12\xaf_m\xf0d\xfeJa\xa4%'





@app.route('/')
def home():
    return render_template('dashboard/home.html')

@app.route('/status')
def status():
    return 'Status: Running'