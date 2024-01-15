import unittest

from test.unit.test_logger import TestLogger


def suite():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    # Automatically discover and add all tests from the TestLogger class
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestLogger))

    return test_suite

if __name__ == "__main__":
    # Run the tests
    unittest.TextTestRunner().run(suite())

