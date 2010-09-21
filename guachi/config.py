from ConfigParser import ConfigParser
from os.path import isfile

class DictMatch(object):

    def __init__(self,config = None,mapped_options = {},mapped_defaults = {}):
        self.config = config 
        self.mapped_options = mapped_options
        self.mapped_defaults = mapped_defaults

    def whatisit(self):
        """Are you a dict, a file or what?"""
        pass 


    def options(self):
        
        # If all fails we will always have default values
        configuration = self.defaults()

        try:
            if self.config == None or isfile(self.config) == False:
                configuration = self.defaults()
                return configuration

        except TypeError:
            if type(self.config) is dict:
                configuration = self.defaults(self.config)
                return configuration
        
        else:
            try:
                converted_opts = {}
                parser = ConfigParser()
                parser.read(self.config)
                file_options = parser.defaults()

                # we are not sure about the section so we 
                # read the whole thing and loop through the items
                for key, value in self.mapped_options.items():
                    try:
                        file_value = file_options[key]
                        converted_opts[value] = file_value
                    except KeyError:
                        pass # we will fill any empty values later with config_defaults
                try:
                    configuration = self.defaults(converted_opts)
                except Exception, error:
                    raise OptionConfigurationError(error)
            except Exception, error:
                raise OptionConfigurationError(error)

        return configuration


    def key_matcher(self, original, mapper=None):
        converted_opts = {}
        if mapper == None:
            mapper = self.mapped_options

        for key, value in mapper.items():
            try:
                file_value = original[key]
                converted_opts[value] = file_value
            except KeyError:
                pass # we will fill any empty values later with config_defaults
        try:
            configuration = self.defaults(converted_opts)
            return configuration
        except Exception, error:
            raise OptionConfigurationError(error)


    def defaults(self, config=None):
        """From the config dictionary it checks missing values and
        adds the defaul ones for them if any"""
        if config == None:
            return self.mapped_defaults()

        for key in self.mapped_defaults.keys():
            try:
                config[key]
                if config[key] == '':
                    config[key] = self.mapped_defaults[key]
            except KeyError:
                config[key] = self.mapped_defaults[key]
        return config


class OptionConfigurationError(Exception):
    """Base class for exceptions in this module."""
    pass
