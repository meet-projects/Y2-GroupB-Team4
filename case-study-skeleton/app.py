from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
    "apiKey": "AIzaSyCCnt5xrueFHh-XyLPWyP6XUZRkpi8tGco",
    "authDomain": "personalproj-ba3c3.firebaseapp.com",
    "projectId": "personalproj-ba3c3",
    "storageBucket": "personalproj-ba3c3.appspot.com",
    "messagingSenderId": "442365273351",
    "appId": "1:442365273351:web:ade388b566ce5b2ebb91a2",
    "databaseURL": "https://y2groupproject-4ae72-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)