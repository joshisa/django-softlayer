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


Management commands
===================

syncstatic
----------

Uploads directories to the cloud storage saving directory structure::

    python manage.py syncstatic

**Options**

* `--mediaroot` - A source directory to copy files from, e.g. "/home/djangoprojects/myproject/media".
Defaults to `settings.MEDIA_ROOT`

* `--noreplace` - Skip and do not replace existing files in the storage. Default is `False`.

* `--mask` - A file mask, e.g. "*.ext". Defaults to: `*.mp3`

* `-v` - higher verbosity is available

get_missing_files
-----------------

Prints information to console about empty or non existing files present in database but not at cloud files storage::

    python manage.py get_missing_files

**Options**

* `--app_model_field` - String containing dot separated app, model and field name. Example: `myapp.User.file`

**NOTE:** this options can be defaulted to `CMD_MISSING_FILES_SETTINGS` variable in `settings.py`::

    CMD_MISSING_FILES_SETTINGS = (
        'app.model.filefield',
        'nextapp.nextmodel.nextfile'
    )

* When it's specified `CMD_MISSING_FILES_SETTINGS` variable you can search a set
of `app.model.field` to search for empty files.

* When using `--app_model_field` option, you can only specify one `app.model.field` per command.


Written by the development team of Arpaso company: http://arpaso.com
