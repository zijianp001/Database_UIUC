"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader



def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """


    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )

    return pool


app = Flask(__name__)
db = init_connection_engine()

index_add_counter = ""

conn = db.connect()

query = 'select Count(*), c.CPUProcess from CPU c NATURAL JOIN Product p where CPUSocket = (select m.Socket from MotherBoard m natural join Product p where ProductName like "ASUS TUF Gaming X470 ATX%%") group by c.CPUProcess'
print(query)
results = conn.execute(query)
keys = results.keys()
items = results.fetchall()
print(keys)
print(items)
conn.close()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
