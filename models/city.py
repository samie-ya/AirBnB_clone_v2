#!/usr/bin/python3
"""
cities module
"""

from models import base_model


class City(base_model.BaseModel):
    """
    class for all cities
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all cities

           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
