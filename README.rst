==========================================
Django storage for SoftLayer Cloud Storage
==========================================

This package uses django-cumulus plus softlayer-object-storage-python packages.

Settings
========

Add the following to your project’s **settings.py** (your SoftLayer credentials)::


    CUMULUS = {
        'USERNAME': 'YourUsername', # your SoftLayer user name
        'API_KEY': 'YourAPIKey',    # SoftLayer api key
        'CONTAINER': 'ContainerName' # SoftLayer container(folder) name
        'NETWORK': 'private', # Paid 'private' or free 'public' network is available
    }

    CLOUD_FILE_STORAGE = 'django_softlayer.SoftLayerStorage'
    INSTALLED_APPS=[
    ...
    'django_softlayer',
    ...]

Usage
=====

To use this storage:

* import storage class, and create your own storage.py::

    from django_softlayer import SoftLayerStorage
    from django.utils.functional import LazyObject
    from django.conf import settings

    class MyStorage(LazyObject):
        def _setup(self):
            self._wrapped = get_storage_class(settings.CLOUD_FILE_STORAGE)()

* Then you can use it in models.py::

    from storage import MyStorage

    class MyModel(Model):
        file = models.FileField(storage=MyStorage())

* That's all.
     
To upload files to storage from folder, check for the command usage::

    ./manage.py syncstatic --help

# Testing

To run tests::

    ./manage.py test django_softlayer


Written by the development team of Arpaso company: http://arpaso.com
