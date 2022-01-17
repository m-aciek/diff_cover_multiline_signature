from unittest import TestCase

from app import call_hello_world


class HelloWorldTests(TestCase):
    def test_greets_world(self):
        self.assertEqual(call_hello_world(), 'Hello world')
