import unittest
import template as sut


@unittest.skip("Don't forget to test!")
class TemplateTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.template_example()
        self.assertEqual("Happy Hacking", result)
