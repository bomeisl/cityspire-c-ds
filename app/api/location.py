#app/location.py



"""Route that provides data for each location based on input of location name in the form of "City, State".

POST '/location/data'
"""


# Imports

import os

from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

import logging
from typing import List, Optional

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, Json


# Router

log = logging.getLogger(__name__)
router = APIRouter()

# Connect to AWS RDS PG DB

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = os.getenv['DATABASE_URL'] # for AWS EB Environment Variable
connection = psycopg2.connect(DATABASE_URL)

# Cursor for making SQL queries

cursor = connection.cursor()


# Instantiate LocationDataRequest BaseModel

class LocationDataRequest(BaseModel):
    """Input Schema - the user's choice of Location (City, State)"""

    location: str = Field(..., example="El Paso, Texas")


# Instantiate LocationDataItem BaseModel

class LocationDataItem(BaseModel):
    """Output Schema - Location information."""
    
    city_name: str = Field(..., example = "Phoenix, Arizona")
    population: int = Field(..., example = 1000000)
    rent_per_month: int = Field(..., example = 1500)
    walk_score: int = Field(..., example = 98)
    livability_score: int = Field(..., example = 1000)

    
# Instantiate LocationDataResponse BaseModel

class LocationDataResponse(BaseModel):
    """Output schema - List of recommended strains."""

    response: Json[LocationDataItem] = Field(...)


# Router to make POST request for data on specified location

@router.post('/location/data', response_model=LocationDataItem)
async def location_data(location: LocationDataRequest):
    """
    Route for front end to obtain the data for the Location of choice.

    ### Request:
    "location": "City, State"

    ### Response:
    A JSON Object of the data for requested Location \n
    "location": city and state of location requested \n
    "population": population of location as an int with no commas \n
    "rent_per_month": rent per month as an int with no $ sign \n
    "walk_score": walk score as a float \n
    "livability_score": livability score as a float
    """

    # Make sure location paramater is a string in the form of "City, State"

    location = str(location)
    location = location.replace('location=', "")
    location = location.replace("'", "")


    # Queries for data response

    #pop_query = """SELECT "2019 Population" FROM CitySpire WHERE "Location" = %s""", [location]
    #rent_query = """SELECT "2019 Rental Rates" FROM CitySpire WHERE "Location" = %s""", [location]
    #walk_query = """SELECT "2019 Walk Score" FROM CitySpire WHERE "Location" = %s""", [location]
    #live_query = """SELECT "2019 Livability Score" FROM CitySpire WHERE "Location" = %s""", [location]

    cursor.execute("""SELECT "2019 Population" FROM cityspire WHERE "Location" = %s;""", [location])
    pop = cursor.fetchone()
    #pop = pop[0][0] # This is slice slice the tuple value from the list of tuples

    cursor.execute("""SELECT "2019 Rental Rates" FROM cityspire WHERE "Location" = %s;""", [location])
    rent = cursor.fetchone()
    #rent = rent[0][0] # This is slice slice the tuple value from the list of tuples

    cursor.execute("""SELECT "Walk Score" FROM cityspire WHERE "Location" = %s;""", [location])
    walk = cursor.fetchone()
    #walk = walk[0][0] # This is slice slice the tuple value from the list of tuples

    cursor.execute("""SELECT "Livability Score" FROM cityspire WHERE "Location" = %s;""", [location])
    live = cursor.fetchone()
    #live = live[0][0] # This is slice slice the tuple value from the list of tuples

    
    # Close the cursor and connection (this breaks the API)

    #cursor.close()
    #connection.close()


    # Return the data that was requested and queried

    return {
        "city_name": str(location),
        "population": int(pop[0]),
        "rent_per_month": int(rent[0]),
        "walk_score": int(walk[0]),
        "livability_score": int(live[0])
    }
