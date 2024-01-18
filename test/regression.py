import unittest

from linter.linter import run_linter
from unit.logger_test import TestLogger
from unit.proxy_handler_test import TestProxyHandler


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogger))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestProxyHandler))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

    run_linter()
