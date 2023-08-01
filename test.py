import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(5)
        self.assertEqual(result, test_param)

    def test_do_stuff2(self):
        test_param = 10
        result = main.do_stuff('hello')
        self.assertTrue(isinstance(result, ValueError))


unittest.main
