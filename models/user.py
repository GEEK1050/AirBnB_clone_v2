#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for MySQL db

    Attributes:
        __tablename__ (str): the name of MySQL table.
        email (SQLAlchemy string): the email of the user.
        password (SQLAlchemy string): the password of the user.
        first_name (SQLAlchemy string): the user's first name
        last_name (SQLAlchemy string): the user's last name
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
