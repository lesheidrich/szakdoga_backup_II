import unittest
from unit.proxy_handler_test import TestProxyHandler
from unit.logger_test import TestLogger


def regression_test() -> unittest.TestSuite:
    """
    Compiles all unit tests into a single runnable regression test
    :return: test suite of all unit tests
    """
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogger))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestProxyHandler))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(regression_test())
