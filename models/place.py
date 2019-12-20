#!/usr/bin/python3
"""This is the place class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    place_amenities = Table("place_amenity", Base.metadata,
                            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

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
    reviews = relationship("Review", cascade="all, delete", backref="reviews_places")
    amenities = relationship("Amenity", secondary="place_amenities", viewonly=False, backref="amaneties_places")

    amenity_ids = []

    @property
    def amenities(self):
        """
        Getter attribute amenities
        :return: the list of Amenity instances, based on
        amenity_ids, linked to place
        """
        amenities_list = []
        objs_ = models.storage.all(models.amenity.Amenity)
        for key in objs_:
            if objs_[key].place_id == self.id:
                amenities_list.append(objs_[key])
        return amenities_list

    @property
    def reviews(self):
        """
        Getter attribute reviews
        :return: the list of reviews
        """
        review_dict = {}
        objs_ = model.storage.all(Review)
        for key, value in objs_.items():
            if value.place_id == self.id:
                review_dict[key] = value
        return review_dict

