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

        self.assertEqual(foo.db_filename, '/tmp/test_guachi')
        self.assertEqual(foo.table, 'data')
        self.assertEqual(foo.select_value, 'SELECT value FROM data WHERE key=?')
        self.assertEqual(foo.select_key, 'SELECT key FROM data WHERE key=?')
        self.assertEqual(foo.update_value, 'UPDATE data SET value=? WHERE key=?')
        self.assertEqual(foo.insert_key, 'INSERT INTO data (key,value) WHERE key=?')
        self.assertEqual(foo.delete_key, 'DELETE FROM data WHERE key=?')
    
