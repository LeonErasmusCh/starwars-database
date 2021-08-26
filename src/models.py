import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(250))
    homeworld =  Column(Integer, ForeignKey('planet.name'))  

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer)
    population = Column(Integer)
    climate = Column(String(100))
    relationPerson = relationship("Person")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    pilot_uid = Column(Integer, primary_key=True)
    name = Column(String(80), ForeignKey('people.name'), nullable=False)
    relationVehicle = relationship("People")

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    people = Column(String(50), ForeignKey('people.name'))
    planet = Column(String(50),ForeignKey('planet.name'))
    vehicle = Column(String(50),ForeignKey('vehicle.name'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50),ForeignKey('favourites'))
    password = Column(String(50))
    relationUser = relationship("Favourites")

   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')