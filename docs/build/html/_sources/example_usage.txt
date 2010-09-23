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
what they are and how we can push them


INI File
--------------
This twitter app will have a INI file so you 
