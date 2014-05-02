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

Run ``pip install aldryn-accordion``.

Add below apps to ``INSTALLED_APPS``: ::

    INSTALLED_APPS = [
        …

        'aldryn_accordion',
        …
    ]
