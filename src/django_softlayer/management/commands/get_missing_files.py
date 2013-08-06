### -*- coding: utf-8 -*- ####################################################
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_app, get_model, FieldDoesNotExist
from django.conf import settings

class Command(BaseCommand):
    '''Calculates similar albums for each album in database'''
    args = ''
    help = 'Returns missing or empty track files from the SoftLayer'
    option_list = BaseCommand.option_list + (
        make_option('--app',
                    dest='app',
                    help='Django application to get models from. Example: myApp'),
        make_option('--model_fields',
                    dest='model_fields',
                    help='String containing dot separated model name and field name\n Example: User.file'),
    )


    def handle(self, app, model_fields, *args, **options):
        self.index = 1
        models = []
        if hasattr(settings, 'CMD_MISSING_FILES_SETTINGS'):
            cmd_settings = settings.CMD_MISSING_FILES_SETTINGS
            app = cmd_settings.get('app', False)
            model_fields = cmd_settings.get('model_fields', False)
            for obj in model_fields:
                models.append(obj.split('.'))

        if not app:
            raise CommandError('You must specify --app option. Example: myApp')
        if not model_fields:
            raise CommandError('You must specify --model_fields option. Example: Model.field')

        def printTrack(obj, reason):
            print "%s. Instance: %s\n\tID: %s\n\tReason: %s" % \
                  (self.index, unicode(obj), obj.pk, reason)
            self.index += 1

        def get_missing_files(model, field_name):
            print '----------------Searching missing or incomplete %ss in %s:--------------\n' % \
                  (field_name, model.__name__)
            for obj in model.objects.all():
                try:
                    if getattr(obj, field_name).file.size == 0:
                        printTrack(obj, 'Size is 0')
                except:
                    printTrack(obj, 'FILE NOT FOUND')
            print '----------------------------------Done--------------------------------------'
        for model_field in models:
            model = get_model(app, model_field[0])
            field_name = model_field[1]
            try:
                model._meta.get_field(field_name)
            except FieldDoesNotExist:
                continue
            get_missing_files(model, field_name)




