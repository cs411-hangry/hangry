import json
import datetime
from api import app
from api import db
#from api.models import restaurant, location, cuisine, rating, checkin
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify

engine = db.engine
conn = engine.connect()

mod = Blueprint('leaderboard', __name__)

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@mod.route('/leaderboard/hot/<user_id>', methods=["GET"])
def get_hot_restaurants(user_id):
    if request.method == "GET":
        try:
            get_hot_restaurants = """
                                    SELECT close_restaurants.restaurant_id, close_restaurants.restaurant_name, AVG(rating.rating), COUNT(checkins)
                                    FROM restaurant, rating, checkins, location,
                                        (SELECT restaurant.restaurant_id, restaurant.restaurant_name
                                        FROM location, restaurant, "user"
                                        WHERE "user".user_id = {0} AND
                                            restaurant.restaurant_id = location.restaurant_id AND
                                            (abs(location.latitude) < 1.001 * abs("user".latitude) AND
                                            abs(location.latitude) > 0.999 * abs("user".latitude)) AND
                                            (abs(location.longitude) < 1.001 * abs("user".longitude) AND
                                            abs(location.longitude) > 0.999 * abs("user".longitude))
                                        ) AS close_restaurants
                                    WHERE close_restaurants.restaurant_id = rating.restaurant_id AND
	                                      close_restaurants.restaurant_id = location.restaurant_id AND
                                          location.location_id = checkins.location_id AND
	                                      checkins.timestamp > '{1}'
                                    GROUP BY close_restaurants.restaurant_id, close_restaurants.restaurant_name
                                    ORDER BY AVG(rating.rating) DESC
                                  """.format(user_id, datetime.datetime.now() - datetime.timedelta(days=14))
            # get_hot_restaurants = """
            # SELECT restaurant.restaurant_id, restaurant.restaurant_name
            #                             FROM location, restaurant, "user"
            #                             WHERE "user".user_id = {0}
            #                                 """.format(user_id)
            result = conn.execute(get_hot_restaurants)
            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = str(row[key])
                restaurants.append(restaurant)
            return jsonify({'restaurants' : restaurants, 'status' : 'success'})
        except Exception as e:
            raise APIError(str(e))

    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /hot requires GET request"})

@mod.route('/leaderboard/top/<user_id>', methods=["POST"])
def get_top_restaurants(user_id):
    if request.method == "POST":
        try:
            data = request.get_json() #request cuisine, number of days
            if data["cuisine_id"] == -1:
                get_top_restaurants = """
                                        SELECT close_restaurants.restaurant_id, close_restaurants.restaurant_name, AVG(rating.rating), COUNT(checkins.timestamp)
                                        FROM serves, restaurant, rating, checkins, location,
                                            (SELECT restaurant.restaurant_id, restaurant.restaurant_name
                                            FROM location, restaurant, "user"
                                            WHERE "user".user_id = {0} AND
                                                restaurant.restaurant_id = location.restaurant_id AND
                                                (abs(location.latitude) < 1.001 * abs("user".latitude) AND
                                                abs(location.latitude) > 0.999 * abs("user".latitude)) AND
                                                (abs(location.longitude) < 1.001 * abs("user".longitude) AND
                                                abs(location.longitude) > 0.999 * abs("user".longitude))
                                            ) AS close_restaurants
                                        WHERE close_restaurants.restaurant_id = rating.restaurant_id AND
    	                                      close_restaurants.restaurant_id = location.restaurant_id AND
                                              location.location_id = checkins.location_id AND
                                              close_restaurants.restaurant_id = serves.restaurant_id AND
    	                                      checkins.timestamp > '{1}'
                                        GROUP BY close_restaurants.restaurant_id, close_restaurants.restaurant_name
                                      """.format(user_id, datetime.datetime.now() - datetime.timedelta(days=int(data['num_days'])))
            else:
                get_top_restaurants = """
                                        SELECT close_restaurants.restaurant_id, close_restaurants.restaurant_name, AVG(rating.rating), COUNT(checkins.timestamp)
                                        FROM serves, restaurant, rating, checkins, location,
                                            (SELECT restaurant.restaurant_id, restaurant.restaurant_name
                                            FROM location, restaurant, "user"
                                            WHERE "user".user_id = {0} AND
                                                restaurant.restaurant_id = location.restaurant_id AND
                                                (abs(location.latitude) < 1.001 * abs("user".latitude) AND
                                                abs(location.latitude) > 0.999 * abs("user".latitude)) AND
                                                (abs(location.longitude) < 1.001 * abs("user".longitude) AND
                                                abs(location.longitude) > 0.999 * abs("user".longitude))
                                            ) AS close_restaurants
                                        WHERE close_restaurants.restaurant_id = rating.restaurant_id AND
    	                                      close_restaurants.restaurant_id = location.restaurant_id AND
                                              location.location_id = checkins.location_id AND
                                              close_restaurants.restaurant_id = serves.restaurant_id AND
                                              serves.cuisine_id = {1} AND
    	                                      checkins.timestamp > '{2}'
                                        GROUP BY close_restaurants.restaurant_id, close_restaurants.restaurant_name
                                      """.format(user_id, data['cuisine_id'], datetime.datetime.now() - datetime.timedelta(days=int(data['num_days'])))

            result = conn.execute(get_top_restaurants)
            restaurants = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = str(row[key])
                restaurants.append(restaurant)
            return jsonify({'restaurants' : restaurants, 'status' : 'success'})
        except Exception as e:
            raise APIError(str(e))

    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /hot requires GET request"})

@mod.route('/leaderboard/map/<user_id>', methods=["GET"])
def get_map_info(user_id):
    if request.method == "GET":
        try:
            get_map_info = """
                            SELECT location.location_id, location.latitude, location.longitude, ts.agg
                            FROM location,
                                (SELECT curr_locations.location_id, STRING_AGG(TO_CHAR(curr_checkins.timestamp,'YYYY-MM-DD HH24:MI:SS.0'), ',') as agg
                                FROM
                                    (SELECT *
                                    FROM location, "user"
                                    WHERE "user".user_id = {0} AND
                                        (abs(location.latitude) < 1.001 * abs("user".latitude) AND
                                            abs(location.latitude) > 0.999 * abs("user".latitude)) AND
                                            (abs(location.longitude) < 1.001 * abs("user".longitude) AND
                                            abs(location.longitude) > 0.999 * abs("user".longitude))
                                    ) AS curr_locations,
                                    (SELECT *
                                    FROM checkins
                                    WHERE checkins.timestamp > '{1}'
                                    ) AS curr_checkins
                                WHERE curr_checkins.location_id = curr_locations.location_id
                                GROUP BY curr_locations.location_id
                                ) AS ts
                            WHERE location.location_id = ts.location_id
                          """.format(user_id, datetime.datetime.now() - datetime.timedelta(days=1))

            result = conn.execute(get_map_info)

            locations  = []
            for row in result:
                loc = {}
                for key in row.keys():
                    loc['location_id'] = row['location_id']
                    loc['latitude'] = row['latitude']
                    loc['longitude'] = row['longitude']
                    loc['timestamp'] = row['agg'].split(",")
                locations.append(loc)

            return jsonify({'locations' : locations, 'status' : 'success'})
        except Exception as e:
            raise APIError(str(e))

    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /hot requires GET request"})
