import unittest
from os import remove, mkdir

from guachi.config  import options, defaults 

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
# Middleware Configuration
guachi.middleware.server_id = 2
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 00000

# Web Interface
guachi.web.host = web.example.com

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s    

# Cache
guachi.cache = 10
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


#    def test_options_TypeError(self):
#        actual = options(config={})
#        expected = self.defaults
#        self.assertEqual(actual, expected)
#
#    def test_options_empty(self):
#        actual = options()
#        expected = self.defaults
#        self.assertEqual(actual, expected)
#
#    def test_options_invalid_file(self):
#        actual = options('/path/to/invalid/file.txt')
#        expected = self.defaults
#        self.assertEqual(actual, expected)
#
#    def test_options_typeError(self):
#        actual = options(['a list should never be passed'])
#        expected = self.defaults
#        self.assertEqual(actual, expected)
#
#    def test_options_Error_string(self):
#        actual = options('a string should never be passed')
#        expected = self.defaults
#        self.assertEqual(actual, expected)
#
#    def test_options_ini(self):
#        actual = options('conf.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'web_port': '80',
#                'cache': '10',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_options_ini_no_id(self):
#        actual = options('conf_two.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '1',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '80',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_options_ini_no_dbhost(self):
#        actual = options('conf_three.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'localhost',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '80',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_options_ini_no_dbport(self):
#        actual = options('conf_four.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': 27017,
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '80',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_options_ini_noapp(self):
#        actual = options('conf_five.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'main',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '80',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_options_ini_no_webhost(self):
#        actual = options('conf_six.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'localhost',
#                'cache': '10',
#                'web_port': '80',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_options_ini_no_webport(self):
#        actual = options('conf_seven.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '8080',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_custom_plugin(self):
#        actual = options('conf_eight.ini')
#        expected = { 
#                'foo' : 'True',
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '8080',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#
#    def test_custom_plugin_none(self):
#        """When bad configured it will not display or get parsed"""
#        actual = options('conf_nine.ini')
#        expected = { 
#                'web_user': False,
#                'plugins': None,
#                'plugin_path': False,
#                'server_id': '2',
#                'db_host': 'remote.example.com',
#                'db_port': '00000',
#                'application': 'secondary',
#                'web_host': 'web.example.com',
#                'cache': '10',
#                'web_port': '8080',
#                'log_level': 'DEBUG',
#                'log_format': '%(asctime)s %(levelname)s %(name)s  %(message)s',
#                'log_datefmt' : '%H:%M:%S'
#                }    
#        self.assertEqual(actual, expected)
#

if __name__ == '__main__':
    unittest.main()
