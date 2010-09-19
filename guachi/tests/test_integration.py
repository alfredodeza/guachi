from os import path, remove
import unittest 

from guachi import ConfigMapper


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.mapped_options = {
            'guachi.db.host':'db_host',
            'guachi.db.port':'db_port',
            'guachi.web.host':'web_host',
            'guachi.web.port':'web_port',
            }

        self.mapped_defaults = {
            'db_host': 'localhost',
            'db_port': 27017,
            'web_host': 'localhost',
            'web_port': '8080',
            }

        try:
            if path.exists('/tmp/guachi'):
                remove('/tmp/guachi')
            else:
                mkdir('/tmp/guachi')
        except Exception:
            pass


    def test_access_mapped_configs(self):
       pass 
