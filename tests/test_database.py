import os
import unittest
from guachi import database

class TestDbdict(unittest.TestCase):
    
    def tearDown(self):
        try:
            os.remove('/tmp/test_guachi')
        except Exception:
            pass 

    def test_create_database(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertTrue(os.path.isfile('/tmp/test_guachi'))

    def test_init(self):
        foo = database.dbdict('/tmp/test_guachi')

        self.assertEqual(foo.path, '/tmp/test_guachi')
        self.assertEqual(foo.table, 'path')
        self.assertEqual(foo.select_value, 'SELECT value FROM data WHERE key=?')

