#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="delete")
    else:
        @property
        def get_city(self):
            print('hi')
            city_dict = models.storage.all(City)
            state_query = State.id
            city_list = []
            for k, v in city_dict.items():
                if v.state_id == State.id:
                    city_list.append(v)
            return city_list
