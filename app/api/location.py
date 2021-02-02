#app/location.py



"""Route that provides data for each location based on input.

POST '/location/data'
"""


# Imports

import pandas as pd
import itertools

import logging
from typing import List, Optional

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

log = logging.getLogger(__name__)
router = APIRouter()


# Import data

df = pd.read_csv("data/pop_rent_crime_walk_cost_livability_bins.csv")

Locations = list(df.Location.unique())


# Instantiate LocationDataRequest BaseModel

class LocationDataRequest(BaseModel):
    """Input Schema - the user's choice of Location (City, State)"""

    location: str = Field(..., example='Orlando, Florida')


# Instantiate LocationDataItem BaseModel

class LocationDataItem(BaseModel):
    """Output Schema - Location information."""
    
    location: str = Field(..., example = 'Orlando, Florida')
    population: int = Field(..., example = 1000000)
    rent_per_month: int = Field(..., example = 1500)
    walk_score: int = Field(..., example = 98.0)
    livability_score: float = Field(..., example = 1000)


# Instantiate LocationDataResponse BaseModel

class LocationDataResponse(BaseModel):
    """Output schema - List of recommended strains."""

    response: LocationDataItem = Field(...)


# Router to make GET request for data on specified location

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

    df[df.Population==location].Location.item()

    return {
        'location': location,
        'population': df[df.Population==location].Location.item(),
        'rent_per_month': df[df.RentalRates==location].Location.item(),
        'walk_score': df[df.WalkScore==location].Location.item(),
        'livability_score': df[df.LivabilityScore==location].Location.item()
    }
        
        #'location': str(location),
        #'population': int(df.loc[df['Location'] == location, '2019 Population']),
        #'rent_per_month': int(df.loc[df['Location'] == location, '2019 Rental Rates']),
        #'walk_score': int(df.loc[df['Location'] == location, 'Walk Score']),
        #'livability_score': float(df.loc[df['Location'] == location, 'Livability Score'])
        