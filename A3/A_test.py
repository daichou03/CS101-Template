import unittest
from A3.A import *

class Test_Assignment(unittest.TestCase):
    def test_A3_1(self):
        self.assertEqual(run_length_encoding("mississippi"), "mis2is2ip2i")

if __name__ == '__main__':
    unittest.main()
