import unittest
from test.linter.linter import run_linter
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

    path = 'C:\\users\\dblin\\PycharmProjects\\WebScraping_and_MonteCarloSim_gwjz4t'
    exceptions = ["linter.py", "regression.py", "main.py"]
    run_linter(path, exceptions)
