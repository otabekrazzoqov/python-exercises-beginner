import unittest
from lesson37home import Shaxs, Talaba

class TestShaxs(unittest.TestCase):
    def setUp(self):
        self.shaxs = Shaxs('Ali', 'Valiyev', 'AA1234567', 1995)

    def test_get_info(self):
        expected_output = 'Ali Valiyev. Passport:AA1234567, 1995-yilda tug`ilgan'
        self.assertEqual(self.shaxs.get_info(), expected_output)

    def test_get_age(self):
        self.assertEqual(self.shaxs.get_age(2022), 27)

class TestTalaba(unittest.TestCase):
    def setUp(self):
        self.talaba = Talaba('Ali', 'Valiyev', 'AA1234567', 1995, '001')

    def test_get_id(self):
        self.assertEqual(self.talaba.get_id(), '001')

    def test_get_bosqich(self):
        self.assertEqual(self.talaba.get_bosqich(), 1)

    def test_get_info(self):
        expected_output = 'Ali Valiyev. 1-bosqich. ID raqami: 001'
        self.assertEqual(self.talaba.get_info(), expected_output)

if __name__ == '__main__':
    unittest.main()
