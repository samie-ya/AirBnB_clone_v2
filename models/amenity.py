#!/usr/bin/python3
"""
amenities module
"""

from models import base_model


class Amenity(base_model.BaseModel):
    """
    class for all Amenities
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all amenities

           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
