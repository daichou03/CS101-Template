import unittest
import A1

class Test_Assignment(unittest.TestCase):
    def test_A1(self):
        self.assertEqual(A1.print_greeting("Roland", 53, True),
                         "Hello Roland. It is your birthday today! Happy birthday! You are 54 years old.")

if __name__ == '__main__':
    unittest.main()
