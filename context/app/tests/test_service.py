from unittest import TestCase

from service import ExampleService


class ServiceTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = ExampleService()

    def test_run(self):
        data = self.service.Data()
        result = self.service.run(data)
        # TODO: make assertion
