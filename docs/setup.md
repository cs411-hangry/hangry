# Set up Documentation

Either provide an env variable for `SQLALCHEMY_DATABASE_URI` which is a postgres URI or we assume that you have a PostgreSQL server running on `localhost` at port `5432`, with the user being `postgres`. In the latter case, we also assume that the database `hangry` has been initialized/created.

To create the database and user
```
psql 
create database hangry owner postgres encoding 'utf-8';
GRANT ALL PRIVILEGES ON DATABASE hangry TO postgres;
```

The following packages are required (developed on Python 3.6.4):

```
alembic==0.9.8
certifi==2018.1.18
chardet==3.0.4
click==6.7
Flask==0.12.2
Flask-Cors==3.0.3
Flask-Login==0.4.1
Flask-Migrate==2.1.1
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
idna==2.6
itsdangerous==0.24
Jinja2==2.10
Mako==1.0.7
MarkupSafe==1.0
psycopg2==2.7.4
python-dateutil==2.7.0
python-editor==1.0.3
requests==2.18.4
six==1.11.0
SQLAlchemy==1.2.5
urllib3==1.22
Werkzeug==0.14.1
``` 

1. Run `python db_create.py`. This will create the tables in the database according to the models defined in `models.py`.
2. Run `python populate.py`. This will populate the tables in the database with some data in the json files in the root directory.
3. Run `python manager.py runserver`. This will run the server for the API at `http://127.0.0.1:5000/`.
4. Do stuff.

If you ever need to start again, just run `db_drop.py` and start the steps again
