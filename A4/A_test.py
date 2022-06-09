import unittest
from A4.A import *

class Test_Assignment(unittest.TestCase):
    def test_A4_1(self):
        write_secret_sentence("cat dog meow")
        f = open("abc123.txt")
        secret_text = f.readline()
        f.close()
        self.assertEqual(secret_text, "c*t d*g m**w")

if __name__ == '__main__':
    unittest.main()
