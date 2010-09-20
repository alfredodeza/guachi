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

    {'module.web.host':'web_host', 'module.web.port':'web_port'}

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

    {'web_host':'localhost', 'web_port':80}

As you can see, we are no longer using INI keys (e.g. ``module.web.host``) but the new keys 
that we assigned.


