from app import app
from flask import render_template
from app.forms import SignUpForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    # Create an instance of the SignUpForm class
    form = SignUpForm()
    # Send that instance to the html as context
    return render_template('signup.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')
