# python tests.py ../source test.test_tzone
from datetime import datetime

from babel.dates import UTC
from tzone import dump, make_timezone, to_local, from_local
from . import TestCase


class TestCaseTZ(TestCase):

    def setUp(self):
        super(TestCaseTZ, self).setUp()
        self.dt = datetime(2017, 8, 24, 0, 0)

    def test_dump(self):
        mask = 'dd.MM.yyyy HH:mm'
        self.assertEqual(dump(self.dt, 'Europe/Moscow', mask), '24.08.2017 03:00')
        self.assertEqual(dump(self.dt, '', mask), '24.08.2017 00:00')

    def test_to_local(self):
        self.assertEqual(to_local(self.dt, ''), self.dt)
        self.assertEqual(to_local(self.dt, 'Europe/Moscow'), datetime(2017, 8, 24, 3, 0))

    def test_from_local(self):
        self.assertEqual(from_local(self.dt, ''), self.dt)
        self.assertEqual(from_local(self.dt, 'Europe/Moscow'), datetime(2017, 8, 23, 21, 0))

    def test_make_timezone(self):
        self.assertEqual(make_timezone(''), UTC)
        self.assertNotEqual(make_timezone('Europe/Moscow'), UTC)
