import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
import sqlalchemy as sa


Base = declarative_base()



class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    is_actived = Column( sa.Boolean(), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

class Persons(Base):
    __tablename__ = 'persons'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)


class PersonsFavorite(Base):
    __tablename__ = 'PersonsFavorite'
    persons_id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)



class PlanetsFavorite(Base):
    __tablename__ = 'PlanetsFavorite'
    planet_id = Column(Integer, ForeignKey("planets.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

 
        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')