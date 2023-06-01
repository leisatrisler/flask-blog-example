from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, LoginForm, PostForm
from app.models import User, Post


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
        # Query the user table to see if there are any users with that username or email
        user_check = db.session.execute(db.select(User).where((User.username==username)|(User.email==email))).scalars().all()
        # If there are any users with username or email, flash a warning message
        if user_check:
            flash('A user with that username and/or email already exists', 'danger')
            return redirect(url_for('signup'))
        # Create a new user
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
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
        # Check to see if there is a user with that username
        user = db.session.execute(db.select(User).where(User.username==username)).scalars().one_or_none()
        # If there is a user AND the password matches that user's hashed password
        if user is not None and user.check_password(password):
            # log the user in via login_user function
            login_user(user)
            flash(f'{username} has successfully logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))


@app.route('/create', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        image_url = form.image_url.data
        print(title, body, image_url, current_user.id)
        # Create an instance of Post with form title and body and the logged in user's id
        new_post = Post(title=title, body=body, user_id=current_user.id)
        # Add the new post to the database
        db.session.add(new_post)
        db.session.commit()
        flash(f'{new_post.title} has been published!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html', form=form)
