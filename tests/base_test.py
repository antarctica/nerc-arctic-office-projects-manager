import unittest

from arctic_office_projects_manager import create_app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.maxDiff = None

    def tearDown(self):
        self.app_context.pop()
