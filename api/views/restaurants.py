import json
from api import app
from api import db
from api.models import Restaurant
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify

engine = db.engine
conn = engine.connect()

mod = Blueprint('restaurants', __name__)

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@mod.route('/restaurants', methods=["GET"])
def get_all_restaurants():
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"restaurant\"")
            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = row[key]
                restaurants.append(restaurant)
            return jsonify({'restaurants' : restaurants})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurants requires GET request"})

@mod.route('/restaurant/<name>', methods=["GET"])
def get_restaurants_by_name(name):
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant.restaurant_name=" + name).format(name)
            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = row[key]
                restaurants.append(restaurant)
            return jsonify({'restaurants' : restaurants})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurants requires GET request"})

@mod.route('/restaurant', methods=["POST"])
def create_restaurant():
    if request.method == "POST":
        try:
            data = request.get_json()
            add_restaurant = "INSERT INTO restaurant (restaurant_name) VALUES ('{0}')".format(data['restaurant_name'])
            result = conn.execute(add_restaurant)
            return jsonify({'status' : 'success', 'message' : 'Created new restaurant!'})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurant requires GET or POST request"})

@mod.route('/restaurant/id/<restaurant_id>', methods=["GET", "DELETE"])
def get_restaurant_by_id(restaurant_id):
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant_id = {}".format(restaurant_id))
            row = result.first()
            if row != None:
                restaurant = {"restaurant_id" : row["restaurant_id"], "restaurant_name" : row["restaurant_name"]}
                return jsonify({'status' : 'success', 'restaurant' : restaurant})
            return jsonify({'status' : 'failed', 'message' : 'No restaurant record found!'})
        except Exception as e:
            raise APIError(str(e))
    elif request.method == "DELETE":
        try:
            result = conn.execute("DELETE FROM \"restaurant\" WHERE restaurant_id = {}".format(restaurant_id))
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant_id = {}".format(restaurant_id))
            row = result.first()
            if row != None:
                return jsonify({"status" : "failed", "message" : "Failed to delete restaurant."})
            return jsonify({"status" : "success", "message" : "Successfully deleted restaurant!"})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurant/id requires GET or POST request"})

@mod.route('/restaurant/cuisines/<cuisine>', methods = ["GET"])
def get_all_restaurant_cuisines(cuisine):
    try:
        result = conn.execute("""
            SELECT food_places.restaurant_name
            FROM (SELECT DISTINCT restaurant_id, cuisine.cuisine_id, cuisine.cuisine_name
            FROM serves
            INNER JOIN cuisine ON serves.cuisine_id = cuisine.cuisine_id) as foods
            , (SELECT DISTINCT restaurant.restaurant_id, restaurant_name
            FROM restaurant
            INNER JOIN serves ON restaurant.restaurant_id = serves.restaurant_id) as food_places
            WHERE upper(foods.cuisine_name) = upper(\'{}\') AND food_places.restaurant_id = foods.restaurant_id""".format(cuisine))
        restaurants = []
        for row in result:
            location = {}
            for key in row.keys():
                location[key] = row[key]
            restaurants.append(location)
        return jsonify({'status':'success', 'restaurants' : restaurants})
    except Exception as e:
        raise APIError(str(e))
