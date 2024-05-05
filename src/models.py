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
    favorite_characters = relationship('Favorites_characters', back_populates='user')
    favorite_planets = relationship('Favorites_planets', back_populates='user')
    favorite_starships = relationship('Favorites_starships', back_populates='user') 

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    gender = Column(String(250), nullable = False)
    height = Column(String(250), nullable = False)
    hair_color = Column(String(250), nullable = False)
    eye_color = Column(String(250), nullable = False)
    birth_year = Column(String(250), nullable = False)
    favorites = relationship('Favorites_characters', back_populates='character')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable = False)
    rotation_period = Column(String(250), nullable = False)
    gravity = Column(String(250), nullable = False)
    population = Column(String(250), nullable = False)
    climate = Column(String(250), nullable = False)
    terrain = Column(String(250), nullable = False)
    favorites = relationship('Favorites_planets', back_populates='planet')
    

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable = False)
    starship_class = Column(String(250), nullable = False)
    manufacturer = Column(String(250), nullable = False)
    length = Column(String(250), nullable = False)
    crew = Column(String(250), nullable = False)
    passengers = Column(String(250), nullable = False)
    favorites = relationship('Favorites_starships', back_populates='starship')

class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    character = relationship('Character', back_populates='favorites')
    user = relationship('User', back_populates='favorite_characters')

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    planet = relationship('Planet', back_populates='favorites')
    user = relationship('User', back_populates='favorite_planets')

class Favorites_starships(Base):
    __tablename__ = 'favorites_starships'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('starships.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    starship = relationship('Starship', back_populates='favorites')
    user = relationship('User', back_populates='favorite_starships')


# ----------------------------------------------------------------
# ----------------------------------------------------------------

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
