import unittest
from A1.A import *

class Test_Assignment(unittest.TestCase):
    def test_A1_1(self):
        self.assertEqual(print_greeting("Damir", 42, False),
                         "Hello Damir. You are 42 years old.")

    def test_A1_2(self):
        self.assertEqual(print_greeting("Roland", 53, True),
                         "Hello Roland. It is your birthday today! Happy birthday! You are 54 years old.")

if __name__ == '__main__':
    unittest.main()
