.. _getting_started:

Getting Started
===================
The most important thing you need to know is that everything in **guachi** is a dictionary.

You treat all your data, keys and values, exactly the same as you would with a Python dictionary.


Dependencies
------------------
There are no dependencies for **guachi** although it is meant to be used with Python versions 2.5 and 
newer.

If you are using Python 2.4 or older this module will not work since we rely on the Sqlite3 bindings 
present in the standar library.

**guachi** is 100% pure Python library!


Most Common Scenario
----------------------
We will cover here a scenario where you have an INI style configuration file where you need to have 
some values that will eventually get stored, and in the case that some values 
are missing you will fill them with defaults. 

At the end, you will be able to view those configurations and access them on the *cheap*.

From now one, we also assume you are importing ``ConfigMapper`` class from **guachi**::

    from guachi import ConfigMapper

Database Location
--------------------
Before anything, you need to decide a location for the database. This can be an existing Sqlite3 
instance or a new one. If there isn't one **guachi** will create one.

There are 2 ways you can provide a path:

 * `/path` : if it is a directory, it will create a database file as `/path/guachi.db`
 * `/path/my_database` : if it is a file it will connect directly without renaming the file.

For simplicity, we will use `/tmp` in the examples that follow, making the actual database location 
`/tmp/guachi.db`.


Set INI mappings
-------------------
These mappings are the ones that will *translate* parsed INI keys into acceptable Python values.
If you have an INI that looks like::

    module.web.host = localhost
    module.web.port = 80

Then you would need to provide **guachi** with a dictionary that maps the keys above to valid dictionary 
keys. Like::

    conf = ConfigMapper('/tmp')
    conf.set_ini_options({'module.web.host':'web_host', 'module.web.port':'web_port'})

You are telling **guachi** how to map the INI keys.


Set Default mappings
----------------------
If your app needs to have defaults then you need to add values to the defaults dictionary so 
**guachi** knows what keys will need to fill in in case they are missing.

.. note::
    If you are not interested in assigning default values you can skip this section.
    **guachi** doesn't need defaults to run.

From the INI file above, we will assume that your app always needs the web host and the port to 
run, so if your user doesn't set them you can supply those values.

So you would have a dictionary that maps the INI values from above to *actual* default values 
for your app, like::

    conf = ConfigMapper('/tmp')
    conf.set_default_options({'web_host':'localhost', 'web_port':80})

As you can see, we are no longer using INI keys (e.g. ``module.web.host``) but the new keys 
that we assigned.


Actual Config Parsing and Mapping
-----------------------------------
Now that you have INI mappings and default ones, you can put your configurations to work.
**guachi** has an engine that figures out the keys and values and sets them accordingly.

You can pass an absolute path to an INI file or a dictionary if you are not dealing with 
files::

    conf = ConfigMapper('/tmp')
    conf.set_config('/path/to/conf.ini')

Or::

    my_conf_dict = {'web_host':'localhost'}
    conf.set_config(my_conf_dict)

Lets suppose your user defined ``web_host`` and nothing else. If you set defaults, the ``web_port``
would get filled in.

There is nothing else to do for *saving* configurations.

Behind the scenes **guachi** can tell if you are passing an INI file or a dictionary and maps everything 
according to the settings we added previously.


Working with values
======================
Now that you have everything in... how do you interact with the values?

Remeber that **guachi** will have all the keys and values but dictionaries will appear (for the most part)
empty when called.

This is basically to avoid the problem we are trying to solve: not having fully loaded dictionaries in memory.


Getting INI options
-----------------------
Remember INI options are the options that translate INI style keys to dictionary keys. Let's retrieve those 
values that we set before in our Python shell::

    >>> conf = ConfigMapper('/tmp')
    >>> ini_dict = conf.get_ini_options()
    >>> ini_dict
    {}
        

what happened? The dict is empty!

Not really, lets try a few dictionary methods on that ``ini_dict`` instance::

    >>> ini_dict.items()
    [(u'module.web.port', u'web_port'), (u'module.web.host', u'web_host')]
    >>> ini_dict.keys()
    [u'module.web.port', u'module.web.host']
    >>> ini_dict['module.web.host']
    u'web_host'
    >>> ini_dict['module.web.port']
    u'web_port'
        
Everything is there... you just need to interact with it.

However... we are also including a method to load the dictionary just in case you are 
too paranoid::

    >>> ini_dict.get_all()
    {u'module.web.port': u'web_port', u'module.web.host': u'web_host'}


Getting Default Options
--------------------------------
Very similar as how we interact with INI options (take a look above) but some of the methods 
change::

    >>> conf = ConfigMapper('/tmp')
    >>> conf.get_default_options()
    {}

    >>> defaults_dict = conf.get_default_options()
    >>> defaults_dict.items()
    [(u'web_port', u'80'), (u'web_host', u'localhost')]
    >>> defaults_dict.keys()
    [u'web_port', u'web_host']

Again, you have access to everything but it is not a *loaded* dictionary, but if you must,
you can load that too::

    >>> defaults_dict.get_all()
    {u'web_port': u'80', u'web_host': u'localhost'}
    

Getting Configuration Values
----------------------------------
Just the method names change in how we access the configuration values, but everything 
we get back behaves the same as before::

    >>> conf_dict = conf.stored_config()
    >>> conf_dict
    {}
    >>> conf_dict.items()
    [(u'web_port', u'80'), (u'web_host', u'localhost')]
    >>> conf_dict.keys()
    [u'web_port', u'web_host']

    >>> conf_dict['web_port']
    u'80'
    >>> conf_dict['web_host']
    u'localhost'
        

As you can see, the default values we assigned at the beginning have been applied and are 
now stored.

And just as before, you can also load the whole thing in memory if you must::

    >>> conf_dict.get_all()
    {u'web_port': u'80', u'web_host': u'localhost'}

There is a helper method for the configs, since it is the one dictionary you are probably 
going to be using more to load the whole dict::

    >>> conf.get_dict_config()
    {u'web_port': u'80', u'web_host': u'localhost'}
    

Modifying Values
------------------
Do you know how to modify values in a dictionary? then you do not need to read this.

**guachi** objects have the **same** methods as a dictionary, so anything goes!

Add key values::

    >>> conf_dict['new_value'] = 'bar'
    >>> conf_dict['new_value'] 
    u'bar'
        
Alter values::

    >>> conf_dict['new_value'] = 'foo'
    >>> conf_dict['new_value']
    u'foo'

Delete::

    >>> del conf_dict['new_value']
    >>> conf_dict['new_value']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "guachi/database.py", line 33, in __getitem__
        if not row: raise KeyError
    KeyError

