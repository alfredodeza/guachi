import os

BASE = """CREATE TABLE data (key PRIMARY KEY, value)"""
OPT_MAP = """CREATE TABLE _guachi_option (key PRIMARY KEY, value)"""
DEF_MAP = """CREATE TABLE _guachi_defaults (key PRIMARY KEY, value)""" 

class Mapper(object):

    def __init__(self, path):
        self.path = self._path_verify(path)

    def set_config_options(self):
        """Maps your INI configuration keys to dictionary keys"""
        pass 

    def set_default_options(self):
        """Maps the default values that we can fill in if keys are empty"""
        pass

    def integrity_check(self):
        """Verify the database is OK"""
        pass

    def _path_verify(self, path):
        """The need to have valid absolute paths"""
        if not os.path.isdir(path):
            return os.path.abspath(path)
        if os.path.isdir(path):
            abspath = os.path.abspath(path)
            return abspath+'/guachi.db'
        else:
            return False 
