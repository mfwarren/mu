Mu
--------

.. image::
    https://secure.travis-ci.org/mfwarren/mu.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/mfwarren/mu

Mu (after Lambda) is a Python Web API Framework specifically for deploying to Amazon Lambda.
It is designed for speed and efficiency, with syntax inspired by the Falcon framework.

Documentation
-------------

Coming as soon as things stabilize

Installation
------------

Mu is limited to Python 2.7 as that is what is available on the Amazon Lambda platform.

Install from PyPI::

    $ pip install mu


Usage
-----

Basic usage::

    $ mu COMMAND APP_MODULE

Where ``APP_MODULE`` is of the pattern ``$(MODULE_NAME):$(VARIABLE_NAME)``. The
module name can be a full dotted path. The variable name refers to an API object
that should be found in the specified module.

Example with test app::

    $ cd examples
    $ mu deploy test:api


License
-------

Mu is released under the MIT License. See the LICENSE_ file for more
details.

.. _LICENSE: http://github.com/mfwarren/mu/blob/master/LICENSE
