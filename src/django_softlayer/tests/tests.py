### -*- coding: utf-8 -*- ####################################################
import inspect, os

from django.test import TestCase
from django.core.management import call_command

from django_softlayer import SoftLayerStorage



class TestSoftLayerStorage(TestCase):

    def setUp(self):
        self.storage=SoftLayerStorage()

    def test_syncstatic_command(self):
        path=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        call_command('syncstatic', mediaroot=os.path.join(path,'test_data'))
        track=self.storage.container.get_object('1.mp3')
        self.assertIsNotNone(track)
        self.assertTrue(self.storage.container.get_object('1.mp3').delete())
