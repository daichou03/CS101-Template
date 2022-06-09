import unittest
import A3.A_test as testSubject  # Change this to change which question to test

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(testSubject)
    unittest.TextTestRunner(verbosity=2).run(suite)
