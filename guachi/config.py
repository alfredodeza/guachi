from ConfigParser import ConfigParser
from os.path import isfile

def options(config=None, mapped_options={}, mapped_defaults={}):
    """Instead of calling ConfigParser all over the place
    we gather, read, parse and return valid configuration
    values for any pacha log.utility here, config should
    always be a file object or None and config_options
    always returns a dictionary with values"""
    
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
            except Exception, e:
                print "Couldn't map configuration: %s" % e

        except Exception, e:
            pass
            print "Couldn't map configuration: %s" % e

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
                config[key] = defaults[key]
        except KeyError:
            config[key] = defaults[key]
    return config
