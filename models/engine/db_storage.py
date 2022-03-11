#!/usr/bin/python3
"""This script will create a new database"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """This class is the beginning of database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """This will initiate the database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """This function will query on the current database session"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        new_dict = {}
        if cls:
            for value in self.__session.query(cls).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
        else:
            for value in self.__session.query(User).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            for value in self.__session.query(Place).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            for value in self.__session.query(State).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            for value in self.__session.query(City).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            # for value in self.__session.query(Amenity).all():
                # name = type(value).__name__ + '.' + value.id
                # new_dict[name] = value
            for value in self.__session.query(Review).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
        return new_dict

    def new(self, obj):
        """This function will add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This function will commit all changes of the current database
           session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """This function will delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """This will create all database features"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
