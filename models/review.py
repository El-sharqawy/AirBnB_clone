#!/usr/bin/python3
"""the Implementation of Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class definition"""

    place_id = ""
    user_id = ""
    text = ""
