#!/usr/bin/python3
"""
states module
"""

from models import base_model


class State(base_model.BaseModel):
    """
    class for all states
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method for all states

           Args:
               args (tuple): This will not be taken into consideration
               kwargs (dict): This will contain the result of to_dict()
        """
        super().__init__(self, *args, **kwargs)
