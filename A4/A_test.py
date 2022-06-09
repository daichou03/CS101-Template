import unittest
from A4.A import *

class Test_Assignment(unittest.TestCase):
    def test_A4_1(self):
        write_secret_sentence("cat dog meow")
        f = open(filename)
        secret_text = f.readline()
        f.close()
        self.assertEqual(secret_text, "c*t d*g m**w")

    @classmethod
    def tearDownClass(cls):
        import os
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    unittest.main()
