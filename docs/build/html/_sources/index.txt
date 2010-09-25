.. guachi documentation master file, created by
   sphinx-quickstart on Sun Sep 19 19:01:10 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

guachi's documentation
==================================

Contents:

.. toctree::
   :maxdepth: 2

   getting_started.rst
   example_usage.rst
   other_uses.rst
   changelog.rst


Persistent Configurations
----------------------------
Instead of re-parsing configuration files every time you need to access
your configurations, make them persistent with **guachi**.

We use a persistent dictionary that writes to a Sqlite3 database. But you 
do not need to know that. 

Everything on your end will look like a dictionary.


Everything is a Dictionary
----------------------------
All configurations are set, modified and used as Python Dictionaries!

The only difference is that they do not live in memory, thus avoiding 
memory issues (dictionaries can be expensive depending on their size).

They are also *lazy* in that these dictionaries appear to be empty, **guachi**
does not load the whole dictionary, but rather, access the keys and values 
as you need.


Set Defaults
--------------
You want to have some defaults and have a way of filling missing configuration 
values? **guachi** can verify there are values missing and do that for you.





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

