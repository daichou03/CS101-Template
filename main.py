import unittest
import A1.A1_test  # Change this to change which question to test

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(A1.A1_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
