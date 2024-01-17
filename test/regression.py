import unittest
from unit.test_logger import TestLogger
from unit.test_proxy_handler import TestProxyHandler


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogger))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestProxyHandler))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
