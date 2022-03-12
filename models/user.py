#!/usr/bin/python3
"""
script for users
"""

from . import base_model


class User(base_model.BaseModel):
    """
    class that defines a User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """The constrictor method for Uuser class

        Args:
            args (tuple): This will not be used
            kwargs (dict): This will contain the result of to_dict
        """
        super().__init__(self, *args, **kwargs)
