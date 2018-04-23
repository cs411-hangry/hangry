from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import jsonify
from api.utils import APIError
import os

UPLOAD_FOLDER = 'photos/'

app = Flask(__name__)

# Setup the SQL Alchmey extension
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:postgres@localhost/hangry")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # TODO: Change this!
jwt = JWTManager(app)

CORS(app)

from api import models

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# import and register blueprints
from api.views import users
app.register_blueprint(users.mod)

from api.views import auth
app.register_blueprint(auth.mod)

from api.views import photos
app.register_blueprint(photos.mod)

from api.views import restaurants
app.register_blueprint(restaurants.mod)

from api.views import locations
app.register_blueprint(locations.mod)

from api.views import cuisines
app.register_blueprint(cuisines.mod)

from api.views import ratings
app.register_blueprint(ratings.mod)

from api.views import serves
app.register_blueprint(serves.mod)

from api.views import checkins
app.register_blueprint(checkins.mod)

from api.views import leaderboard
app.register_blueprint(leaderboard.mod)
