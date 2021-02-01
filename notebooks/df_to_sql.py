# df_to_sql.py



# Imports

import os

import pandas as pd
from dotenv import load_dotenv
import sqlalchemy
import psycopg2
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
import pprint


# Load environment variables aka secrets from .env

load_dotenv()

# Read in data for the DB

df = pd.read_csv("cityspire-c-ds/data/pop_rent_crime_walk_cost_livability_bins.csv")

# Instantiate DB

database_url = os.getenv('DATABASE_URL')

# Connect to the DB

engine = sqlalchemy.create_engine(database_url)
connection = engine.connect()

# Create get_url function to verify connection to the DB and get the URL

def get_url():
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname
    
    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}

# Get the URL

get_url()

# Function to write data to a table in the DB

def write_data(df):
    tablename = 'cityspire'
    df.to_sql(tablename, connection, if_exists='append', index=False, method='multi')

# Write the data to a table in the DB

write_data(df)

# Create read_date function to read data from the table in the DB

def read_data():
    query = """SELECT * FROM cityspire LIMIT 5"""
    df = pd.read_sql(query, connection)
    return pprint.pprint(df.to_dict(orient='records'))

read_data()
