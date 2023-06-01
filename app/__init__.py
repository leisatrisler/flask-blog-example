from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Create an instance of SQLAlchemy to connect our app to the database
db = SQLAlchemy(app)
# Create an instance of Migrate that will track our db and app
migrate = Migrate(app, db)

# import all of the routes from the routes file and models from the models file into the current package
from app import routes, models
