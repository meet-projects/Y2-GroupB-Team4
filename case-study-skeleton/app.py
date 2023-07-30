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

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('index'))
        except:
             error = "Authentication failed"
    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"email": request.form['email']}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('index'))
        except:
             return "Authentication failed"
    return render_template("signup.html")

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)