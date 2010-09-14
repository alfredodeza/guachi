import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup

tests_require = ['nose']

setup(
    name = "guachi",
    version = "0.0.1",
    packages = ['guachi'],
    include_package_data=True,
    package_data = {
        '': ['distribute_setup.py'],
        },

    # metadata 
    author = "Alfredo Deza",
    author_email = "alfredodeza [at] gmail [dot] com",
    description = "Global, persistent configurations as dictionaries",
    long_description = """\
When projects start to grow, the need for a globally accessible configuration
manager is obvious.

Having configurations mapped to dictionaries is really useful, but can create a 
problem with memory.

**Guachi** not only holds persistent dictionaries on disk, but it also maps 
INI style keys to dictioanry keys, and can fill in the default values if some 
of them are missing.
""",
   classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],

    license = "MIT",
    keywords = "configuration management persistent dictionaries dictionary parse map mapping",
    url = "http://code.google.com/p/guachi",   

)

