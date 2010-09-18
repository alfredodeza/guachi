import unittest
from os import remove, mkdir

from guachi.config  import options, defaults, OptionConfigurationError 

def setup():
    try:
        remove('/tmp/guachi')
    except Exception:
        pass
    #mkdir('/tmp/guachi')

    txt = open('/tmp/guachi/conf.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.server_id = 2
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 00000

# Web Interface
guachi.web.host = web.example.com
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s

# Cache
guachi.cache = 10
    """
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_two.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 00000

# Web Interface
guachi.web.host = web.example.com
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s    

# Cache
guachi.cache = 10
"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_three.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.server_id = 2
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.port = 00000

# Web Interface
guachi.web.host = web.example.com
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s    

# Cache
guachi.cache = 10
"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_four.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.server_id = 2
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.host = remote.example.com

# Web Interface
guachi.web.host = web.example.com
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s    

# Cache
guachi.cache = 10
"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_five.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.server_id = 2

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 00000

# Web Interface
guachi.web.host = web.example.com
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s    

# Cache
guachi.cache = 10
"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_six.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.server_id = 2
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 00000

# Web Interface
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s    

# Cache
guachi.cache = 10
"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_seven.ini', 'w')
    text = """
[DEFAULT]

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 0

"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_eight.ini', 'w')
    text = """
[DEFAULT]
# Database (Mongo)
guachi.db.host = example.com 
guachi.db.port = 

# Web Interface
guachi.web.host = 
guachi.web.port = 


"""
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_nine.ini', 'w')
    text = """
[DEFAULT]
# Database (Mongo)
guachi.db.host = 
guachi.db.port = 

# Web Interface
guachi.web.host = 
guachi.web.port = 

"""
    txt.write(text)
    txt.close()


def teardown():
    try:
        remove('/tmp/guachi') 
    except Exception:
        pass


class TestConfigOptions(unittest.TestCase):

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


    def test_options_config_none_empty_defaults(self):
        """No config and no defaults should return an empty dict"""
        actual = options()
        expected = {}
        self.assertEqual(actual, expected)


    def test_options_config_invalid_empty_defaults(self):
        """Invalid config file and no defaults should return an empty dict"""
        actual = options(config='/path/to/invalid/file')
        expected = {}
        self.assertEqual(actual, expected)


    def test_options_config_dict_empty_defaults(self):
        """A dict config and no defaults should return an empty dict"""
        actual = options(config={})
        expected = {}
        self.assertEqual(actual, expected)


    def test_options_from_dict(self):
        """Pass a dict with no values and get defaults back"""
        actual = options(config={}, mapped_defaults=self.mapped_defaults)
        expected = self.mapped_defaults
        self.assertEqual(actual, expected) 


    def test_options_from_file_empty_options(self):
        """A conf file with empty values should get values filled in"""
        actual = options('/tmp/guachi/conf_nine.ini', self.mapped_options, self.mapped_defaults)
        expected = self.mapped_defaults
        self.assertEqual(actual, expected) 


    def test_options_from_file_one_option(self):
        """A conf file with one value should get values filled in"""
        actual = options('/tmp/guachi/conf_eight.ini', self.mapped_options, self.mapped_defaults)
        expected = {
            'db_host': 'example.com',
            'db_port': 27017,
            'web_host': 'localhost',
            'web_port': '8080',
            }

        self.assertEqual(actual, expected) 

    
    def test_options_from_file_empty_defaults(self):
        """Just one default should not overwrite other config values"""
        actual = options('/tmp/guachi/conf_eight.ini', self.mapped_options, {})
        expected = {
            'db_host': 'example.com',
            'db_port': '',
            'web_host': '',
            'web_port': '',
            }

        self.assertEqual(actual, expected) 


    def test_options_key_error_passes(self):
        """When options are missing options() passes on the KeyError"""
        actual = options('/tmp/guachi/conf_seven.ini', self.mapped_options, self.mapped_defaults)
        expected = {
            'db_host': 'remote.example.com',
            'db_port': '0',
            'web_host': 'localhost',
            'web_port': '8080',
            }

        self.assertEqual(actual, expected) 

        
    def test_options_from_file_raise_error(self):
        """Just one default should not overwrite other config values"""
        self.assertRaises(OptionConfigurationError, options, '/tmp/guachi/conf_eight.ini', self.mapped_options, '')  


if __name__ == '__main__':
    unittest.main()
