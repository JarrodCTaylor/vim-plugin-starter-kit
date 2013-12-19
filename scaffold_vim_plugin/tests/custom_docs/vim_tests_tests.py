import unittest
import vim_tests as sut


@unittest.skip("Don't forget to test!")
class VimTestsTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_tests_example()
        self.assertEqual("Happy Hacking", result)
