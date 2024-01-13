from unittest import TestCase

from web import app


class WebTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_run(self):
        # TODO: update template
        pass
