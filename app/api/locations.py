#app/locations.py



"""Route that provides locations the model was trained on.
GET '/locations'
"""


# Imports

import pandas as pd

import logging
from typing import List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

log = logging.getLogger(__name__)
router = APIRouter()


# Import data

df = pd.read_csv("data/pop_rent_crime_walk_cost_livability_bins.csv")

Locations = list(df.Location.unique())


# Instantiate LocationsResponse BaseModel

class LocationsResponse(BaseModel):
    """Use this data model to parse the request body JSON."""

    locations: List[str] = Field(..., example=['Orlando, Florida', 'Portland, Oregon', "..."])


# Router to make GET request for labels of data

@router.get('/locations', response_model=LocationsResponse)
async def locations():
    """Route for front end to obtain the Locations the model was trained on.
    ### Response
    - `locations`: list of locations in form of City, State
    """
    return {
        'locations': Locations
    }
