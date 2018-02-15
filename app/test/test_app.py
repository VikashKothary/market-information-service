#!/usr/bin/env python3
"""
test_app.py - Tests for app.py
"""

from app import app

import unittest


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_flask_set_up(self):
        response = self.app.get('/success')
        self.assertEqual(response.data, b"App is working")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()
