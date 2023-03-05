import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name("abbos", "abduganiyev")
        self.assertEqual(name, "Abbos Abduganiyev")
        
        
        
unittest.main()        