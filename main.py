import unittest
import A4.A_test as testSubject  # Change this to change which question to test

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(testSubject)
    unittest.TextTestRunner(verbosity=2).run(suite)
