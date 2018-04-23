# Endpoint Documentation


## User

**Endpoint**

    GET /users

This returns all of the users in our Users table. It returns each column for each user.

**Response**
```
{
    "users": [
        {
            "email": "abdalla6@illinois.edu",
            "latitude": 40.1059,
            "longitude": -88.243385,
            "name": "Abdi Abdalla",
            "password": "password",
            "user_id": 1,
            "username": "abdi"
        },
        .
        .
        .
    ]
}
```
**Endpoint**

    GET /user/id/<user_id>

This searches the Users relation by the user_id criterion, and either returns the corresponding user or nothing.

**Response**
```
{
    "status": "success",
    "user": {
        "email": "abdalla6@illinois.edu",
        "latitude": 40.1059,
        "longitude": -88.243385,
        "name": "Abdi Abdalla",
        "password": "password",
        "user_id": 1,
        "username": "abdi"
    }
}
```

**Endpoint**

    DELETE /user/username/<user_id>

This searches the Users relation by the user_id criterion, and either deletes the corresponding user or does nothing.

**Response**

```
{
    "message": "Successfully deleted user!",
    "status": "success"
}
```


**Endpoint**

    GET /user/username/<username>

This searches the Users relation by the username criterion, and either returns the corresponding user or nothing.
**Response**
```
{
    "status": "success",
    "user": {
        "email": "abdalla6@illinois.edu",
        "latitude": 40.1059,
        "longitude": -88.243385,
        "name": "Abdi Abdalla",
        "password": "password",
        "user_id": 1,
        "username": "abdi"
    }
}
```

**Endpoint**

    DELETE /user/username/<username>

This searches the Users relation by the username criterion, and either deletes the corresponding user or does nothing.

**Response**

```
{
    "message": "Successfully deleted user!",
    "status": "success"
}
```

**Endpoint**

    POST /user

Creates a new user in the User table given the correct input.

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| email | string |   **Required** | test1@gmail.com
| username | string |   **Required** | test1
| password | string | **Required** | fakepassword
| name | string | Can be NULL | Test Person
| latitude | float | Can be NULL | 40.12891
| longitude | float | Can be NULL | -87.3202

This input must be passed in the form of JSON, as below:

```
{
	"username" : "test1",
	"email" : "test1@gmail.com",
	"password" : "fakepassword",
	"name" : "Test Person",
	"latitude" : 40.00,
	"longitude" : -87.00
}
```

**Response**

```
{
    "message": "Created new user!",
    "status": "success"
}
```

## Auth

**Endpoint**

    POST /login

Logs a user in, given correct credentials, and creates a session for the user. Requires the username and password as input.

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| username | string |   **Required** | test1
| password | string | **Required** | fakepassword

```
{
    "username": "test1",
    "password": "fakepassword"
}
```

**Response**

```
{
    "message": "User [username] successfully logged in!",
    "status": "success"
}
```

**Endpoint**

    GET /logout

Logs a user out, and ends their session.

**Response**

```
{
    "message": "User [username] successfully logged out!",
    "status": "success"
}
```

**Endpoint**

    POST /signup

Intended for the signup flow. Creates a new user in the User table given the correct input (and the username and email aren't already taken).

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| email | string |   **Required** | test1@gmail.com
| username | string |   **Required** | test1
| password | string | **Required** | fakepassword

This input must be passed in the form of JSON, as below:

```
{
	"username" : "test1",
	"email" : "test1@gmail.com",
	"password" : "fakepassword"
}
```

**Response**

```
{
    "message": "Created new user!",
    "status": "success"
}
```

## Restaurant

**Endpoint**

    GET /restaurants

This returns all of the restaurants in our Restaurants table. It returns each column for each restaurant.

**Response**
```
{
    "restaurants": [
        {
            "restaurant_id": 1,
            "restaurant_name": "McDonalds"
        },
        .
        .
        .
    ]
}
```
**Endpoint**

    GET /restaurant/id/<restaurant_id>

This searches the Restaurant relation by the restaurant_id criterion, and either returns the corresponding restaurant or nothing.

**Response**
```
{
    "status": "success",
    "restaurant": {
        "restaurant_id": 1,
        "restaurant_name": "McDonalds"
    }
}
```

**Endpoint**

    GET /restaurant/name/<restaurant_name>

This searches the Restaurant relation by the restaurant_name criterion, and either returns all corresponding restaurants or nothing.

**Response**
```
{
    "restaurants": [
        {
            "restaurant_id": 1,
            "restaurant_name": "McDonalds"
        },
        .
        .
        .
    ]
}
```

**Endpoint**

    DELETE /restaurant/id/<restaurant_id>

This searches the Restaurant relation by the restaurant_id criterion, and either deletes the corresponding restaurant or does nothing.

**Response**

```
{
    "message": "Successfully deleted restaurant!",
    "status": "success"
}
```

**Endpoint**

    DELETE /restaurant/name/<restaurant_name>

This searches the Restaurant relation by the restaurant_name criterion, and either deletes all the corresponding restaurants with the given name or does nothing.

**Response**

```
{
    "message": "Successfully deleted all instances of restaurant!",
    "status": "success"
}
```

**Endpoint**

    POST /restaurant

Creates a new user in the User table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| restaurant_id | int |   **Required** | 1
| restaurant_name | string |   **Required** | McDonalds

This input must be passed in the form of JSON, as below:

```
{
  "restaurant_id": 1,
  "restaurant_name": "McDonalds"
}
```

**Response**

```
{
    "message": "Created new restaurant!",
    "status": "success"
}
```

## Location

**Endpoint**

    GET /locations  **INCOMPLETE**

This returns all of the locations in our Locations table.

**Response**

```
{
    "locations": [
        {
            "latitude": 40.1298,
            "location_id": 1,
            "longitude": -88.2582,
            "restaurant_id": 1,
            "restaurant_name": Dos Reales
            "avg": 3
        },
        {
            "latitude": 40.118377,
            "location_id": 2,
            "longitude": -88.243698,
            "restaurant_id": 2,
            "restaurant_name": Destihl
            "avg": 4
        },
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    GET /locations/restaurant/<restaurant_id>  **INCOMPLETE**

This searches the Location relation by the restaurant_id criterion, and either returns the corresponding restaurant location(s) or nothing.

**Response**
```
{
    "locations": [
        {
            "latitude": 40.105828,
            "location_id": 6,
            "longitude": -88.195036,
            "restaurant_id": 6,
            "restaurant_name": Huaraches Moroleon
            "avg": 4
        }
    ],
    "status": "success"
}
```

**Endpoint**

    GET /locations/cuisine/<cuisine_id>  **INCOMPLETE**

This searches the Location relation by the cuisine_id criterion, and either returns the corresponding restaurant location(s) or nothing.

**Response**
```
{
    "locations": [
        {
            "latitude": 40.105828,
            "location_id": 6,
            "longitude": -88.195036,
            "restaurant_id": 6,
            "restaurant_name": Huaraches Moroleon
            "avg": 4
        }
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    GET /locations/zipcode/<zipcode>

This searches the Location relation by the zipcode criterion, and either returns the corresponding restaurant location(s) or nothing.

**Response**
```
{
    "locations": [
        {
            "address": "805 S Philo Rd, Urbana 61801",
            "city": "Urbana",
            "country": "USA",
            "latitude": 40.105828,
            "location_id": 6,
            "longitude": -88.195036,
            "restaurant_id": 6,
            "zipcode": "61801"
        }
    ],
    "status": "success"
}
```

**Endpoint**

    GET /locations/city/<city>

This searches the Location relation by the city criterion, and either returns the corresponding restaurant location(s) or nothing.

**Response**
```
{
    "locations": [
        {
            "address": "805 S Philo Rd, Urbana 61801",
            "city": "Urbana",
            "country": "USA",
            "latitude": 40.105828,
            "location_id": 6,
            "longitude": -88.195036,
            "restaurant_id": 6,
            "zipcode": "61801"
        }
    ],
    "status": "success"
}
```

**Endpoint**

    DELETE /locations/<location_id>

This searches the Restaurant relation by the location_id criterion, and either deletes all the corresponding locations with the given name or does nothing.

**Response**

```
{
    "message": "successfully deleted location",
    "status": "success"
}
```

**Endpoint**

    POST /location

Creates a new location in the Location table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| restaurant_id | int |   **Required** | 4
| address | string |   can be NULL | 1234 N. Fake Street
| zipcode | string |   can be NULL | 12345
| city | string |   can be NULL | Fakeopolis
| country | string |   can be NULL | FAKE
| latitude | float |   can be NULL | 43.53343
| longitude | float |   can be NULL | -87.09898


This input must be passed in the form of JSON, as below:

```
{
	"restaurant_id" : 4,
	"address" : "1234 N. Fake Street",
	"zipcode" : "12345",
	"city" : "Fakeopolis",
	"country" : "FAKE",
	"latitude" : 43.53343,
	"longitude" : -87.09898
}
```

**Response**

```
{
    "message": "Successfully added location!",
    "status": "success"
}
```

## Serves

**Endpoint**

    GET /serves/restaurant/<restaurant_id>

This searches the Serves relation by the restaurant_id criterion, and either returns all the cuisines served by the specified restaurant.

**Response**
```
{
    "cuisines": [
        {
            "cuisine_id": 23,
            "cuisine_name": "International"
        },
        {
            "cuisine_id": 24,
            "cuisine_name": "Japanese"
        },
        {
            "cuisine_id": 25,
            "cuisine_name": "Sushi"
        }
    ],
    "restaurant_id": "4",
    "status": "success"
}
```

**Endpoint**

    GET /serves/cuisine/<cuisine_id>

This searches the Serves relation by the cuisine_id criterion, and either returns all the restaurants that serve a specific cuisine.

**Response**
```
{
    "cuisine_id": "24",
    "restaurants": [
        {
            "restaurant_id": 4,
            "restaurant_name": "Kofusion"
        },
        {
            "restaurant_id": 46,
            "restaurant_name": "Yellowfin"
        },
        {
            "restaurant_id": 51,
            "restaurant_name": "Sushi Kame"
        },
        {
            "restaurant_id": 53,
            "restaurant_name": "Oishi"
        }
    ],
    "status": "success"
}
```

**Endpoint**

    GET /locations/zipcode/<zipcode>

This searches the Location relation by the zipcode criterion, and either returns the corresponding restaurant location(s) or nothing.

**Response**
```
{
    "locations": [
        {
            "address": "805 S Philo Rd, Urbana 61801",
            "city": "Urbana",
            "country": "USA",
            "latitude": 40.105828,
            "location_id": 6,
            "longitude": -88.195036,
            "restaurant_id": 6,
            "zipcode": "61801"
        }
    ],
    "status": "success"
}
```

**Endpoint**

    DELETE /serves/<serves_id>

This searches the Serves relation by the serves_id criterion, and either deletes all the corresponding serving information or does nothing.

**Response**

```
{
  'status' : 'success',
  'message' : 'Successfully deleted serves entry.'
}
```

**Endpoint**

    POST /serves

Creates a new serving information in the Serves table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| restaurant_id | int |   **Required** | 100
| cuisine_id | int |   **Required** | 20



This input must be passed in the form of JSON, as below:

```
{
    "restaurant_id": 100,
    "cuisine_id": 20
}
```

**Response**

```
{
    "message": "Created serves entry!",
    "status": "success"
}
```

## Cuisine

**Endpoint**

    GET /cuisines

This returns all the cuisines in our database.

**Response**
```
{
    "cuisines": [
        {
            "cuisine_id": 1,
            "cuisine_name": "American"
        },
        {
            "cuisine_id": 2,
            "cuisine_name": "Pizza"
        },
        {
            "cuisine_id": 3,
            "cuisine_name": "Burger"
        },
        .
        .
        .,
        {
            "cuisine_id": 50,
            "cuisine_name": "Cafe"
        },
        {
            "cuisine_id": 51,
            "cuisine_name": "Pub Food"
        },
        {
            "cuisine_id": 52,
            "cuisine_name": "Soul Food"
        }
    ],
    "status": "success"
}
```

**Endpoint**

    GET /cuisine/<cuisine_id>

This searches the Cuisine relation by the cuisine_id criterion, and returns the name of that cuisine.

**Response**
```
{
    "cuisine_id": 50,
    "cuisine_name": "Cafe",
    "status": "success"
}
```

**Endpoint**

    DELETE /cuisine/<cuisine_id>

This searches the Cuisine relation by the cuisine_id criterion, and deletes the corresponding cuisine.

**Response**

```
{
  'status' : 'success',
  'message' : 'Successfully deleted cuisine!'
}
```

**Endpoint**

    POST /cuisine

Creates a new cuisine in the Cuisine table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| cuisine_name | string |   **Required** | Abdis cuisine



This input must be passed in the form of JSON, as below:

```
{
    "cuisine_name": "Abdis Cuisine"
}
```

**Response**

```
{
    "message": "Successfully created cuisine!",
    "status": "success"
}
```

**Endpoint**

    PUT /cuisine

Updates the cuisine name for a specified cuisine.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| cuisine_id | int |   **Required** | 54
| cuisine_name | string |   **Required** | Somali



This input must be passed in the form of JSON, as below:

```
{
    "cuisine_name": 54,
    "cuisine_name": "Somali"
}
```

**Response**

```
{
    "message": "Successfully updated cuisine!",
    "status": "success"
}
```

## Photo

**Endpoint**

    GET /photos/user/<user_id>

This searches the Photos relation by the user_id criterion, and returns the list of photos by the user.

**Response**

```
{
    "photos": [
        {
            "photo_id": 3
            "photo_path": "https://i.imgur.com/VekfqoA.jpg",
            "restaurant_id": 4,
            "user_id": 4,
            "timestamp": "some time"
        },
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    GET /photos/restaurant/<restaurant_id>

This searches the Photos relation by the restaurant_id criterion, and returns the list of photos associated with the restaurant.

**Response**

```
{
    "photos": [
        {
            "photo_id": 3
            "photo_path": "https://i.imgur.com/VekfqoA.jpg",
            "restaurant_id": 4,
            "user_id": 4,
            "timestamp": "some time"
        },
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    DELETE /photos/<photo_id>

This searches the Photos relation by the photo_id criterion, and deletes the corresponding photo from our database.

**Response**

```
{
    'status' : 'success',
    'message' : 'Successfully deleted photo!'
}
```

**Endpoint**

    POST /photos

Upload a photo to our database, and link it with a user and restaurant.

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| user_id | string |   **Required** | 4
| restaurant_id | string |   **Required** | 76
| image_url | string | **Required** | "https://i.imgur.com/dlkfslA.jpg"

This input must be passed in the form of JSON, as below:

```
{
	"user_id" : 4,
	"restaurant_id" : 76,
	"image_url" : "https://i.imgur.com/dlkfslA.jpg"
}
```

**Response**

```
{
    "message": "Successfully uploaded image!",
    "status": "success"
}
```

## Rating

**Endpoint**

    GET /ratings/user/<user_id>

This searches the rating relation by the user_id criterion, and returns all the ratings given by the specified user.

**Response**
```
{
    "ratings": [
        {
            "rating": 4,
            "rating_id": 1,
            "restaurant_id": 1,
            "timestamp": "sometime",
            "user_id": 1
            "restaurant_id": name
        },
        {
            "rating": 4,
            "rating_id": 2,
            "restaurant_id": 2,
            "timestamp": "sometime",
            "user_id": 1
            "restaurant_id": name
        },
        .
        .
        .,
        {
            "rating": 3,
            "rating_id": 100,
            "restaurant_id": 100,
            "timestamp": "sometime",
            "user_id": 1
            "restaurant_id": name 
        }
    ],
    "status": "success"
}
```

**Endpoint**

    GET /ratings/restaurant/<restaurant_id>

This searches the rating relation by the restaurant_id criterion, and returns all the ratings for a specified restaurant.

**Response**
```
{
    "ratings": [
        {
            "rating": 4,
            "rating_id": 1,
            "restaurant_id": 1,
            "timestamp": "sometime",
            "user_id": 1
        },
        {
            "rating": 4,
            "rating_id": 2,
            "restaurant_id": 2,
            "timestamp": "sometime",
            "user_id": 1
        },
        .
        .
        .,
        {
            "rating": 3,
            "rating_id": 100,
            "restaurant_id": 100,
            "timestamp": "sometime",
            "user_id": 1
        }
    ],
    "status": "success"
}
```

**Endpoint**

    GET /ratings/<rating_id>

This searches the Rating relation by the rating_id criterion, and returns the corresponding rating object.

**Response**
```
{
    "rating": {
        "rating": 4,
        "rating_id": 1,
        "restaurant_id": 1,
        "timestamp": "sometime",
        "user_id": 1
    },
    "status": "success"
}
```

**Endpoint**

    DELETE /ratings/<rating_id>

This searches the Rating relation by the rating_id criterion, and deletes the corresponding rating object.

**Response**

```
{
  'status' : 'success',
  'message' : 'Successfully deleted rating!'
}
```

**Endpoint**

    PUT /ratings/<rating_id>/<rating>

This searches the Rating relation by the rating_id criterion, and updates the rating with the new rating.

**Response**

```
{
  'status' : 'success',
  'message' : 'Successfully updated rating!'
}
```

**Endpoint**

    POST /ratings

Creates a new rating in the Rating table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| rating | int |   **Required** | 5
| restaurant_id | int |  **Required** | 100
| user_id | int |   **Required** | 87


This input must be passed in the form of JSON, as below:

```
{
	"rating": 5,
    "restaurant_id": 100,
    "user_id": 87
}
```

**Response**

```
{
  'status' : 'success',
  'message' : 'Successfully created rating!'
}
```

## Checkins

**Endpoint**

    GET /checkin

This returns all of the checkins in our Checkins table.

**Response**

```
{
    "checkins": [
        {
            "checkin_id": 1,
            "user_id": 1,
            "location_id": 1,
            "timestamp": 2018-04-22 15:35:07
        },
        {
            "checkin_id": 2,
            "user_id": 1,
            "location_id": 3,
            "timestamp": 2018-04-22 15:35:07
        },
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    GET /checkin/id/<user_id>

This returns checkins corresponding to user_id

**Response**

```
{
    "checkins": [
        {
            "checkin_id": 1,
            "user_id": 1,
            "location_id": 1,
            "timestamp": 2018-04-22 15:35:07
        },
        {
            "checkin_id": 2,
            "user_id": 1,
            "location_id": 3,
            "timestamp": 2018-04-22 15:35:07
        },
        .
        .
        .
    ],
    "status": "success"
}
```


**Endpoint**

    GET /checkin/location/<user_id>  **INCOMPLETE**

This returns locations corresponding to user_id

**Response**

```
{
  "locations": [
        {
            "location_id": 6
            "latitude": 40.1059,
            "longitude": -88.243385,
            "restaurant_name": 'Murphy's'
        }
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    POST /checkin

Creates a new checkin in the Checkins table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| location_id | int |  **Required** | 100
| user_id | int |   **Required** | 87


This input must be passed in the form of JSON, as below:

```
{
    "location_id": 100,
    "user_id": 87
}
```

**Response**

```
{
  'status' : 'success',
  'message' : 'Successfully created checkin!'
}
```

## Leaderboard

**Endpoint**

    GET /hot/<user_id>

This returns all of the trending restaurants based on average rating and number of checkins

**Response**

```
{
    "restaurants": [
        {
            "restaurant_id": 4,
            "restaurant_name": "Kofusion"
            "count": 4
            "avg" : 3.17
        },
        ...
    ],
    "status": "success"
}
```
**Endpoint**

    GET /top/<user_id>  **INCOMPLETE**

This returns all of the trend restaurants based on average rating and number of checkins. Needs cuisine_id and num_days as input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| cuisine_id | int | Can be NULL | 10
| num_days | int | Can be NULL | 14


This input must be passed in the form of JSON, as below:

```
{
    "cuisine_id": 10,
    "num_days": 14
}
```

**Response**

```
{
    "restaurants": [
        {
            "restaurant_id": 4,
            "restaurant_name": "Kofusion"
            "rating": 4
            "checkins" : 10
        },
        ...
    ],
    "status": "success"
}
```
**Endpoint**

    GET /map/<user_id>

This returns all of the trending restaurants based on average rating and number of checkins

**Response**

```
{
    "locations": [
          {
              "location_id": 6
              "latitude": 40.1059,
              "longitude": -88.243385,
              "timestamps": [
                  2018-04-22 15:35:07,
                  2018-04-20 04:20:00
              ],
          },
          ...
      ]
}
```
