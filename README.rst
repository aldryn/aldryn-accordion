================
Aldryn Accordion
================

Plugin allows to define accordion, each item might have another items.


Installation
============

Aldryn Platform Users
---------------------

Choose a site you want to install the add-on to from the dashboard. Then go to ``Apps -> Install app`` and click ``Install`` next to ``Accordion`` app.

Redeploy the site.

Manuall Installation
--------------------

::

    ``pip install -e git+git://github.com/aldryn/aldryn-accordion.git#egg=aldryn_accordion``

Add ``aldryn_accordion`` to ``INSTALLED_APPS``.

Configure ``aldryn-boilerplates`` (https://pypi.python.org/pypi/aldryn-boilerplates/).

To use the old templates, set ``ALDRYN_BOILERPLATE_NAME='legacy'``.
To use https://github.com/aldryn/aldryn-boilerplate-standard (recommended, will be renamed to
``aldryn-boilerplate-bootstrap3``) set ``ALDRYN_BOILERPLATE_NAME='bootstrap3'``.

When using the ``legacy`` boilerplate, **jQuery** and
`classjs <https://github.com/finalangel/classjs-plugins>`_ cl.accordion are required.
