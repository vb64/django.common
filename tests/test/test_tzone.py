# python tests.py ../source test.test_tzone
from datetime import datetime

from tzone import dump
from . import TestCase


class TestCaseTZ(TestCase):

    def test_dump(self):
        mask = 'dd.MM.yyyy HH:mm'
        self.assertEqual(dump(datetime(2017, 8, 24, 0, 0), 'Europe/Moscow', mask), '24.08.2017 03:00')
        self.assertEqual(dump(datetime(2017, 8, 24, 0, 0), '', mask), '24.08.2017 00:00')
