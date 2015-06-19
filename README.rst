====================
django-smart-save
====================

Make ``save`` call ``full_clean``.

Do you think Django models ``save`` method will validate all fields
(i.e. call ``full_clean``) before saving or any time at all? Wrong!

I discovered this awful truth when I couldn't understand why
a model object with an email field (without `blank=True`) could be
saved with an empty string as email address.

More info:

* "Why doesn't django's model.save() call full clean?"
    http://stackoverflow.com/questions/4441539/
* "Model docs imply that ModelForm will call Model.full_clean(), but it won't."
    https://code.djangoproject.com/ticket/13100


Installing
==========

First add the application to your Python path. The easiest way is to use
`pip`::

    pip install django-smart-save

You should install by downloading the source and running::

    $ python setup.py install

Configuring
-----------

Make sure you have `django.contrib.auth` installed, and add the `smart_save`
application to your `INSTALLED_APPS` list::

    INSTALLED_APPS = (
        ...
        'django.contrib.auth',
        'smart_save',
    )

You can specify a different method name in your project settings (default: save_if_valid):

    SMART_SAVE_METHOD = 'my_save'


Usage Overview
==============

It is simple::

    >>> user = User(username="chris")
    >>> user.save_if_valid()
    True
    >>> user = User(username="")
    >>> user.save_if_valid()
    False
    >>> user._errors
    {'username': ['This field cannot be blank.']}

License
=======

Anyone is free to use or modify this software under the terms of the BSD
license.
