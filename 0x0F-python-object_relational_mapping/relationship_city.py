#!/usr/bin/python3

"""
This is a script that contains the class
definition of a 'City'
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """City class
    Attr:
        __tablename__ (str): Tablename of class
        id (Int): id of the class
        name (str): name of the class
        state_id (int): foreign key. the state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
