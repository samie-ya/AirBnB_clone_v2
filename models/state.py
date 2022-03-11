#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ This class will create a class called State"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        def cities(self):
            """This function returns the list of City instances with
               state_id equals to the current State.id
            """
            from models import storage
            from models.city import City
            new_list = []
            for key, value in storage.all(City):
                if (value.id == self.id):
                    new_list.append(value)
            return new_list
