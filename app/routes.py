from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the SignUpForm class
    form = SignUpForm()
    # Check if the request is POST and the form is valid
    if form.validate_on_submit():
        print('HOORAY OUR FORM IS VALIDATED!')
        # If valid, get the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, username, email, password)
        # flash a message saying user has signed up
        flash(f"{username} has signed up for the blog!", 'success')
        # Redirect back to the home page
        return redirect(url_for('index'))
    # Send that instance to the html as context
    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Form Validated!')
        username = form.username.data
        password = form.password.data
        print(username, password)
        # mimic checking credentials
        if username != 'brians' or password != 'abc123':
            flash('Invalid username and/or email', 'danger')
            return redirect(url_for('login'))
        else:
            flash(f'{username} has successfully logged in', 'success')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)
