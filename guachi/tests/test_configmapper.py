import os
import unittest

from guachi import ConfigMapper
from guachi.database import dbdict

class test_ConfigMapper(unittest.TestCase):

    def setUp(self):
        try:
            os.remove('/tmp/guachi.db')
            os.remove('/tmp/foo_guachi.db')
        except Exception:
            pass 

    def tearDown(self):
        try:
            os.remove('/tmp/guachi.db')
            os.remove('/tmp/foo_guachi.db')
        except Exception:
            pass 


    def test_init(self):
        foo = ConfigMapper('/tmp')
        expected = '/tmp/guachi.db'
        actual = foo.path 
        self.assertEqual(actual, expected) 


    def test_set_config_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'config.db.port':'db_port'}
        foo.set_config_options(my_config)
        db = dbdict(path='/tmp/guachi.db', table='_guachi_options')
        expected = my_config
        actual = db.get_all()
        self.assertEqual(actual, expected) 


    def test_set_default_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'db_port':1234}
        foo.set_default_options(my_config)
        db = dbdict(path='/tmp/guachi.db', table='_guachi_defaults')
        expected = my_config
        actual = db.get_all()
        self.assertEqual(actual, expected) 


    def test_get_config_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'config.db.port':'db_port'}
        foo.set_config_options(my_config)
        actual = foo.get_config_options()
        expected = my_config
        self.assertEqual(actual, expected) 


    def test_get_default_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'db_port':1234}
        foo.set_default_options(my_config)
        actual = foo.get_default_options()
        expected = my_config
        self.assertEqual(actual, expected) 
