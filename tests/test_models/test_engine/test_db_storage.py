#!/usr/bin/python3
''' Unit tests for DB storage '''
import os
import time
import json
import sys
import io
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.db_storage import DBStorage
from console import HBNBCommand

class testDBStorage(unittest.TestCase):
    '''
    Testing the DB storage class
    '''
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Only want to test Database storage")
    def test_existence(self):
        '''
        '''
        pass
#        storage = DBStorage()
#        storage.reload()
#        user = User(name="binita")
#        my_dict = storage.all(User)
#        for k, v in my_dict:
#            self.assertTrue("
