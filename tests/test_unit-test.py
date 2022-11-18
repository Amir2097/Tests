import unittest
from YA import new_folder

etalon = 204

class TestFunc(unittest.TestCase):
    def test_new_folder(self):
        result = new_folder(123)
        self.assertEqual(result, etalon)