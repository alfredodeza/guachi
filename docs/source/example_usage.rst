.. _example_usage:

Usage Examples
================
Here we provide a few examples on how to use **guachi** with some applications.


Lets assume we have a Twitter application and we need to store some things like:

 * username (text)
 * update frequency (integers)
 * load at startup (boolean)

Lets see how our example app can use **guachi** to leverage user configurations.


Database Location
---------------------
Before anything else, remember **guachi** uses a single-file database via Sqlite3.
This means that you need to provide a path for it.

For our little app we will create it as a hidden file in the users directory::

    from os import environ
    
    home = environ.get('HOME')
    config_db_path = home+'/.twitter.db'

The above in my system resolves to: ``/Users/alfredo/.twitter.db``


Setting Defaults
-----------------
The twitter application needs some defaults to run properly, so lets make sure 
what they are and how we can push them to **guachi**.

We want the frequency to be set at every 120 seconds and for our app to load
at startup::

    {'frequency':120, 'load':True}


INI File
--------------
This twitter app will have a INI file so the user can make changes to the app.

The INI file for this app looks like this::

    [DEFAULT]
    
    app.twitter.username =
    app.update.frequency = 
    app.load.startup = 


And we will be using the following path to refer to it: ``/Users/alfredo/.twitter.ini``

Setting INI Mappings
-----------------------
The INI file will be filled with user values, but first, lets mapp those horrible 
long names to short ones so they are easier to read within our app.

Although this step is entirely optional, it is nice to have shorter names, so lets create 
another dictionary with the names we want::

    
    ini_mappings = {
        'app.twitter.username' : 'username',
        'app.update.frequency : 'frequency',
        'app.twitter.startup' : 'startup'
        }

This means that our app will not care about names like ``app.twitter.username`` to retrieve 
values, but rather just ``username``.


Setting our Values
=====================
Now that we have made a few decisions like:

 * INI File options 
 * INI options mappings 
 * Default options for our app 
 * Absolute path for the database file 

We are ready to set them, and this needs to happen just once (things are persistent here remember?)::

    from guachi import ConfigMapper 
    from os import environ
    
    home = environ.get('HOME')
    config_db_path = home+'/.twitter.db'
    defaults = {'frequency':120, 'load':True}
    ini_mappings = {
        'app.twitter.username' : 'username',
        'app.update.frequency : 'frequency',
        'app.twitter.startup' : 'startup'
        }


    conf = ConfigMapper(config_db_path)
    conf.set_default_options(defaults)
    conf.set_ini_options(ini_mappings) 
    

The code above took care of setting everything for our app, we are ready for some user interaction now.


User Interaction
------------------
Now that our twitter app has been installed, the user can start adding configuration to 
the INI file. Let's take a look at the INI file and how it looks::

    [DEFAULT]
    
    app.twitter.username = alfredodeza
    app.update.frequency = 60
    app.load.startup = False

Now we have a few things that have changed. We have a username, a different frequency 
and a different setting for the startup option.

.. note::
    From now on, we will assume you are importing ConfigMapper from guachi to avoid
    redundancy in the examples.

Lets deal with that::

    ini_file = ``/Users/alfredo/.twwiter.ini``
    conf = ConfigMapper(config_db_path)
    conf.set_config(ini_file)

That's it! At this point, **guachi** has parsed the config file and stored the values.

Lets query them calling our keys::

    >>> db_conf = conf.stored_config()
    >>> db_conf['frequency']
    60 

Great, we now are making sure we have our data. We can actually get that value from anywhere 
in our twitter app by calling it this way::

    db = ConfigMapper(config_db_path)
    conf = db.stored_config()

    frequency = conf['frequency']


Getting Deafults
---------------------
Above we inspected an INI file with some changed values. But what happens when the user 
has none?

Since we set our defaults, we can be sure they are right there in case our app needs 
it in some sub-module::

    >>> db = ConfigMapper(config_db_path)
    >>> conf = db.stored_config()
    >>> conf['load']
    True


Updating Values 
-----------------
What if a user makes changes? We can always save and update what we read from the INI 
file at load time, to make sure we have the latest changes from the user::

    conf = ConfigMapper(config_db_path)
    conf.update_config(ini_file)



Conclusions
---------------
You should now be able to create and manage an instance of **guachi**. Remember though, that 
although we are storing the values in a database, **guachi** returns dictionary objects,
so any interaction you want with the keys or values, can be done just as if you were 
dealing with one.

