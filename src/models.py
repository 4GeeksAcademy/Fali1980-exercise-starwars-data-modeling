import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    email = Column (String, nullable=False, unique=True)
    password = Column (String(10)) 

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    gender = Column(String(250), nullable = False)
    height = Column(Integer, primary_key=True)
    hair_color = Column(String(250), nullable = False)
    eye_color = Column(String(250), nullable = False)
    birth_year = Column(Integer, primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, primary_key=True)
    rotation_period = Column(Integer, primary_key=True)
    gravity = Column(String(250), nullable = False)
    population = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable = False)
    terrain = Column(String(250), nullable = False)
    

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable = False)
    starship_class = Column(String(250), nullable = False)
    manufacturer = Column(String(250), nullable = False)
    length = Column(Integer, primary_key=True)
    crew = Column(Integer, primary_key=True)
    passengers = Column(Integer, primary_key=True)

class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favorites_starships(Base):
    __tablename__ = 'favorites_starships'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('starships.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


# ----------------------------------------------------------------
# ----------------------------------------------------------------

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
