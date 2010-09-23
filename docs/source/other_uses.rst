.. _other_uses:

Other Uses
===========
Although **guachi** usually expects dictionary objects as input, it can 
also work with *dictionary-like* objects.

This is very common in Web Frameworks like Turbogears and Pylons, where 
configuration gets handled by paste.

Turbogears
---------------
Turbogears holds everything in memory in a dictionary-like object which is 
usually accessible if you grab it like::

    from tg import config 

The ``config`` object looks like a dictionary but it doesn't evaluate as one.

**guachi** will still try to loop through the keys and values and map them correctly.

So if you have a few options parsed by the framework, you should not have any 
issues passing the ``config`` object in ::

    from tg import config 
    from guachi import ConfigMapper

    my_opts = ConfigMapper('/tmp')
    my_opts.set_config(config)

Although this section is specific to Turbogears, you should be able to apply the same 
for any other Framework that uses Paste as a configuration manager or anything that 
has a dictioanry-like object.
