from ConfigParser import ConfigParser
from os.path import isfile

def options(config=None, mapped_options={}, mapped_defaults={}):
    
    # If all fails we will always have default values
    configuration = defaults()

    try:
        if config == None or isfile(config) == False:
            configuration = defaults()
            return configuration

    except TypeError:
        if type(config) is dict:
            configuration = defaults(config, mapped_defaults)
    
    else:
        try:
            converted_opts = {}
            parser = ConfigParser()
            parser.read(config)
            file_options = parser.defaults()

            # we are not sure about the section so we 
            # read the whole thing and loop through the items
            for key, value in mapped_options.items():
                try:
                    file_value = file_options[key]
                    converted_opts[value] = file_value
                except KeyError:
                    pass # we will fill any empty values later with config_defaults
            try:
                configuration = defaults(converted_opts, mapped_defaults)
            except Exception, error:
                raise OptionConfigurationError(error)
        except Exception, error:
            raise OptionConfigurationError(error)

    return configuration


def defaults(config=None, mapped_defaults={}):
    """From the config dictionary it checks missing values and
    adds the defaul ones for them if any"""
    if config == None:
        config = {}

    for key in mapped_defaults.keys():
        try:
            config[key]
            if config[key] == '':
                config[key] = mapped_defaults[key]
        except KeyError:
            config[key] = mapped_defaults[key]
    return config


class OptionConfigurationError(Exception):
    """Base class for exceptions in this module."""
    pass
