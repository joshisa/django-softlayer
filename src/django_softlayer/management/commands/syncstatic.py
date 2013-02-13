### -*- coding: utf-8 -*- ####################################################

import os
import datetime
import sys
import object_storage
import fnmatch
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
from django.core.files import File
from django.utils.encoding import force_unicode
from django.utils._os import safe_join
from django.utils.importlib import import_module

from pytils.translit import slugify
from django_softlayer import SoftLayerStorage

from music.utils import parse_item

class Command(BaseCommand):
    '''Walks the directory specified in MEDIA_FOLDER and uploads mp3 files to storage'''
    args = ''
    help = 'Walks the directory and uploads mp3 files to cloud storage container'
    
    option_list = BaseCommand.option_list + (
        make_option('--mediaroot',
            default=settings.MEDIA_ROOT,
            help='A source directory to copy files from, e.g. "/home/djangoprojects/myproject/media".'),
        make_option('--mask',
            default='*.mp3',
            help='A file mask, e.g. "*.mp3".'),
    )
    
    def handle(self, mediaroot, mask, *args, **options):
        
        verbosity = int(options.get('verbosity', 1))
        
        storage=SoftLayerStorage()
        total = 0
        for root, dirnames, filenames in os.walk(mediaroot):
            for filename in fnmatch.filter(filenames, mask):
                file_name = os.path.abspath(os.path.join(root, filename))
        
                relative_name = os.path.relpath(file_name, mediaroot)
                
                with open(file_name, 'rb') as _file:
                    storage.save(relative_name, File(_file))
    
                if verbosity > 1:
                    total += 1
                    print '{0}: {1}'.format(total, file_name)
