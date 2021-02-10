#app/db.py



"""Database functions"""

#Imports

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
import psycopg2
from psycopg2.extras import execute_values
import json


# Router

router = APIRouter()


# Load environment variables aka secrets from .env

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = os.getenv['DATABASE_URL'] # for AWS EB Environment Variable

# Connect to AWS RDS PG DB with FastAPI on Heroku (Hosted on AWS)

connection = psycopg2.connect(DATABASE_URL)


# Cursor for making SQL queries

cursor = connection.cursor()


# Get a SQLAlchemy database connection (we are using Postgres...)

async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    load_dotenv()
    database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
    engine = sqlalchemy.create_engine(database_url)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


# Verify we can connect to the database

@router.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname

    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}


# This looks like trash and it is slow, but it is a start for a more refined serve of data

@router.get('/cityspire')
async def get_table(connection=Depends(get_db)):
    """Return table of all data from CitySpire DB in json object"""
    select_query = "SELECT * from CitySpire"
    cursor.execute(select_query)
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return json.dumps(records)


# Elastic Load Balancing health checks

@router.get('/healthcheck')
def healthcheck():
    msg = ("This is a health check message.")
    return {"message": msg}
