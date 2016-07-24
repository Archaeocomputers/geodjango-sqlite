from django.test import TestCase
from .load import run

class LoadTests(TestCase):
    def test_loadscript(self):
        run()
