.. _changelog:

Changelog
==========

0.0.5
--------

 * Minor release with only one fix: more verbose exceptions. Before, KeyError exceptions 
   where raised without a message. This version should be a bit more explicit as to what
   is causing the exception.

0.0.4
-------

 * Changed the way tables are created when connecting to a new database. Before, if the 
   database file didn't exist, guachi would create the tables, but this creates issues 
   when connecting to existing databases so for now, the SQL is ``CREATE TABLE IF NOT EXISTS``

0.0.3
--------

 * Fixes a bug where a non existent path or a path that holds no keys for a config file 
   would not return a dictionary with defaults.
