import os
import sqlite3
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
        self.assertEqual(foo.insert_key_value, 'INSERT INTO data (key,value) VALUES (?,?)')
        self.assertEqual(foo.delete_key, 'DELETE FROM data WHERE key=?')

    def test_get_item_keyerror(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertRaises(KeyError, foo.__getitem__, 'meh')

    def test_get_item(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'beer'
        self.assertEqual(foo['bar'], u'beer')
 
    def test_setitem_typeerror(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertRaises(sqlite3.InterfaceError, foo.__setitem__, 'bar', {'a':'b'})

    def test_delitem_keyerror(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertRaises(KeyError, foo.__delitem__, 'meh')

    def test_delitem(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'beer'
        self.assertEqual(foo['bar'], 'beer')
        del foo['bar']
        self.assertRaises(KeyError, foo.__delitem__, 'bar')

    def test_key_empty(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertEqual(foo.keys(), [])

    def test_keys(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'beer'
        self.assertEqual(foo.keys(), ['bar'])

    def test_integrity_check_true(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertTrue(foo._integrity_check())

        
