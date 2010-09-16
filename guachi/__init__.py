from guachi.database import dbdict
import os

class Mapper(object):

    def __init__(self, path):
        self.path = self._path_verify(path)

    def set_config_options(self, dictionary):
        """Maps your INI configuration keys to dictionary keys"""
        db = dbdict(self.path, table='_guachi_options') 
        for key, value in dictionary.items():
            db[key] = value 


    def set_default_options(self, dictionary):
        """Maps the default values that we can fill in if keys are empty"""
        db = dbdict(self.path, table='_guachi_defaults') 
        for key, value in dictionary.items():
            db[key] = value

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

