#!/usr/bin/python3
"""the Implementation of place Class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class definition"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    max_gues = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []