#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os

class Place(BaseModel, Base):
    """ This creates a class called Place """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    #amenities = relationship("Amenity", secondary=for_relationship,
    #                         viewonly=False)
    #amenity_ids = []

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def reviews(self):
            """This function returns the list of Review instances with
               place_id equals to the current Place.id
            """
            from models import storage
            from models.review import Review
            new_list = []
            for key, value in storage.all(Review).items():
                if (value.id == self.id):
                    new_list.append(value)
            return new_list
