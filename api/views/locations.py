import os
from api import app
from api import db
from api.models import User
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify
from flask_login import LoginManager, login_required, login_user, logout_user

engine = db.engine
conn = engine.connect()

mod = Blueprint('locations', __name__)

@mod.route('/locations', methods = ["GET"])
def get_all_locations():
    try:
        query = """
                SELECT locs.location_id, locs.latitude, locs.longitude, locs.restaurant_id, locs.restaurant_name, rat.avg
                FROM (SELECT location.location_id, location.latitude, location.longitude, location.restaurant_id, restaurant.restaurant_name
                    FROM location, restaurant
                    WHERE location.restaurant_id = restaurant.restaurant_id
                    )AS locs,
                    (SELECT restaurant.restaurant_id, AVG(rating.rating) AS avg
                    FROM restaurant, rating
                    WHERE rating.restaurant_id = restaurant.restaurant_id
                    GROUP BY restaurant.restaurant_id
                    )AS rat
                WHERE locs.restaurant_id = rat.restaurant_id
                """
        result = conn.execute(query)
        locations = []
        for row in result:
            location = {}
            for key in row.keys():
                if key == "avg":
                    location[key] = str(row[key])
                else:
                    location[key] = row[key]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/restaurant/<restaurant_id>', methods = ["GET"])
# def get_all_restaurant_locations(restaurant_id):
#     try:
#         # query = """
#         #         SELECT locs.location_id, locs.latitude, locs.longitude, locs.restaurant_id, locs.restaurant_name, rat.avg
#         #         FROM
#         #             (SELECT location.location_id, location.latitude, location.longitude, location.restaurant_id, restaurant.restaurant_name, AVG(rating.rating)
#         #             FROM location, restaurant
#         #             WHERE location.restaurant_id = restaurant.restaurant_id AND
#         #                 restaurant.restaurant_id = {}
#         #             )AS locs,
#         #             (SELECT restaurant.restaurant_id, AVG(rating.rating) AS avg
#         #             FROM restaurant, rating
#         #             WHERE rating.restaurant_id = restaurant.restaurant_id
#         #             GROUP BY restaurant.restaurant_id
#         #             )AS rat,
#         #         WHERE
#         #             locs.restaurant_id = rat.restaurant_id
#         #         """.format(restaurant_id)
#         query = """
#             SELECT DISTINCT location.location_id, location.latitude, location.longitude, restaurant.restaurant_id AS yo, location.restaurant_id, restaurant.restaurant_name
#                 FROM location, restaurant
#                 WHERE location.restaurant_id = restaurant.restaurant_id AND location.restaurant_id=""" + restaurant_id
#         result = conn.execute()
#         locations = []
#         for row in result:
#             location = {}
#             for key in row.keys():
#                 location[key] = row[key]
#             locations.append(location)
#         return jsonify({'status':'success', 'locations' : locations})
#     except Exception as e:
#         raise APIError(str(e))

@mod.route('/locations/restaurant/<restaurant_id>', methods = ["GET"])
def get_all_restaurant_locations(restaurant_id):
    try:
        # query = """
        #         SELECT locs.location_id, locs.latitude, locs.longitude, locs.restaurant_id, locs.restaurant_name, rat.avg
        #         FROM
        #             (SELECT location.location_id, location.latitude, location.longitude, location.restaurant_id, restaurant.restaurant_name, AVG(rating.rating)
        #             FROM location, restaurant
        #             WHERE location.restaurant_id = restaurant.restaurant_id AND
        #                 restaurant.restaurant_id = {}
        #             )AS locs,
        #             (SELECT restaurant.restaurant_id, AVG(rating.rating) AS avg
        #             FROM restaurant, rating
        #             WHERE rating.restaurant_id = restaurant.restaurant_id
        #             GROUP BY restaurant.restaurant_id
        #             )AS rat,
        #         WHERE
        #             locs.restaurant_id = rat.restaurant_id
        #         """.format(restaurant_id)
        query = """
                SELECT DISTINCT location.location_id, location.latitude, location.longitude, restaurant.restaurant_id AS yo, location.restaurant_id, restaurant.restaurant_name
                    FROM location, restaurant
                    WHERE location.restaurant_id = restaurant.restaurant_id AND location.restaurant_id=""" + restaurant_id

        result = conn.execute(query)
        locations = []
        for row in result:
            location = {}
            for key in row.keys():
                location[key] = row[key]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/zipcode/<zipcode>', methods = ["GET"])
def get_all_zipcode_locations(zipcode):
    try:
        result = conn.execute("SELECT * FROM location WHERE zipcode = \'{}\'".format(zipcode))
        locations = []
        for row in result:
            location = {}
            location["location_id"] = row["location_id"]
            location["restaurant_id"] = row["restaurant_id"]
            location["address"] = row["address"]
            location["zipcode"] = row["zipcode"]
            location["city"] = row["city"]
            location["country"] = row["country"]
            location["latitude"] = row["latitude"]
            location["longitude"] = row["longitude"]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/city/<city>', methods = ["GET"])
def get_all_city_locations(city):
    try:
        result = conn.execute("SELECT * FROM location WHERE city = \'{}\'".format(city))
        locations = []
        for row in result:
            location = {}
            location["location_id"] = row["location_id"]
            location["restaurant_id"] = row["restaurant_id"]
            location["address"] = row["address"]
            location["zipcode"] = row["zipcode"]
            location["city"] = row["city"]
            location["country"] = row["country"]
            location["latitude"] = row["latitude"]
            location["longitude"] = row["longitude"]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/cuisine/<cuisine_id>', methods = ["GET"])
def get_location_data_given_cuisine(cuisine_id):
        try:
            query = """
                    SELECT location.location_id, location.latitude, location.longitude, location.restaurant_id, food_stuffs.restaurant_name
                    FROM location,
                        (SELECT food_places.restaurant_id, food_places.restaurant_name
                        FROM (SELECT DISTINCT restaurant_id, cuisine.cuisine_id, cuisine.cuisine_name
                            FROM serves
                            INNER JOIN cuisine ON serves.cuisine_id = cuisine.cuisine_id) as foods,
                            (SELECT DISTINCT restaurant.restaurant_id, restaurant_name
                            FROM restaurant
                            INNER JOIN serves ON restaurant.restaurant_id = serves.restaurant_id) as food_places
                        WHERE foods.cuisine_id = {} AND
                            food_places.restaurant_id = foods.restaurant_id
                        ) AS food_stuffs
                    WHERE location.restaurant_id = food_stuffs.restaurant_id
                    """.format(cuisine_id)
            result = conn.execute(query)
            locations = []
            for row in result:
                location = {}
                for key in row.keys():
                    location[key] = row[key]
                locations.append(location)
            return jsonify({'status':'success', 'locations' : locations})
        except Exception as e:
            raise APIError(str(e))

@mod.route('/locations/<location_id>', methods = ["DELETE"])
def delete_location(location_id):
    try:
        result = conn.execute("DELETE FROM location WHERE location_id = {}".format(location_id))
        return jsonify({'status':'success', 'message' : 'successfully deleted location'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/location', methods = ["POST"])
def create_location():
    data = request.get_json()
    try:
        result = conn.execute("INSERT INTO location (restaurant_id, address, zipcode, city, country, latitude, longitude) VALUES ({0}, \'{1}\', \'{2}\', \'{3}\', \'{4}\', {5}, {6})".format(data["restaurant_id"], data["address"], data["zipcode"], data["city"], data["country"], data["latitude"], data["longitude"]))
        return jsonify({'status':'success', 'message' : 'Successfully added location!'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/id/<location_id>', methods = ["GET"])
def get_id_locations(location_id):
    try:
        query = """
                SELECT DISTINCT location.location_id, location.latitude, location.longitude FROM location WHERE location_id=""" + location_id

        result = conn.execute(query)
        locations = []
        for row in result:
            location = {}
            for key in row.keys():
                location[key] = row[key]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))
