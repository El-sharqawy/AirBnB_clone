#!/usr/bin/python3
"""the Implementation of User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class definition"""

    first_name = ""
    last_name = ""
    email = ""
    password = ""
