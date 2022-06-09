import unittest
from A2.A import *

class Test_Assignment(unittest.TestCase):
    def test_A2_1(self):
        self.assertEqual(validate_ipv4_address("130.216.57.164"), True)

    def test_A2_2(self):
        self.assertEqual(validate_ipv4_address("130.-216.57.164"), False)

if __name__ == '__main__':
    unittest.main()
