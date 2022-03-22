#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os


for_relationship = Table('place_amenity', Base.metadata,
                         Column('place_id', String(60),
                                ForeignKey('places.id'), primary_key=True,
                                nullable=False),
                         Column('amenity_id', String(60),
                                ForeignKey('amenities.id'), primary_key=True,
                                nullable=False))


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
    amenities = relationship("Amenity", secondary=for_relationship,
                             viewonly=False)
    amenity_ids = []

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

        @property
        def amenities(self):
            """returns the list of Amenity instances based on the attribute
               amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            from models.amenity import Amenity
            new_list = []
            for key, value in storage.all(Amenity).items():
                for i in amenity_id:
                    if (i == value.id):
                        new_list.append(value)
            return new_list

        @amenities.setter
        def amenities(self, obj):
            """append method for adding an Amenity.id to the attribute
               amenity_ids
            """
            if obj:
                Place.amenity_ids.append(obj.id)
