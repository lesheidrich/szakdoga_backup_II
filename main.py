# Example usage
import os
import re
from datetime import datetime

from log.logger import Logger
from scraper.proxy.proxy_handler import ProxyHandler
from secrets import PROJECT_FOLDER

if __name__ == "__main__":
    print(PROJECT_FOLDER)


    """
    regression:
    loader = unittest.TestLoader()

    # Replace 'path/to/your/project' with the actual path to your project directory
    project_directory = 'path/to/your/project'

    # Creating a test suite using discover
    suite = loader.discover(project_directory, pattern='test_*.py')

    # Running the test suite
    unittest.TextTestRunner().run(suite)
    
    
    
    ***TESTRUNNER
    unittest.TextTestRunner().run(suite)
    should be able to run tests and integrate with logger
    """





    # h = ProxyHandler("proxies_test.csv")
    # working_proxy_list = h.process_proxies()


    """
    TODO:
    - CI: github
    - linter
    
    - proxy
    - proxy unit test
    
    - regression test
    - integration test
    
    - webscraper
        - a) requests + bs4 + pd
        - b) requests + bs4
        - c) selenium + -> a & b
        - d) selenium only (maybe scrap)
        - unittest + integration test
    - scrapy
    - unittest + integration test
    
    
    - sql alchemy db handler
    - unittest + integration test
    
    
    """


    # logger = Logger(name='MyAppLogger', log_level="INFO")
    #
    # logger.info("This is an informational message.")
    # logger.warning("This is a warning message.")
    # logger.error("This is an error message.")
    #
    # print("reading")
    # # with open("./log/application_log.log", 'r') as f:
    # #     content = f.read()
    # # print(content)
    # print(logger.get_content())
    # print("done")
    #
    # l = Logger(name="test", log_file="test.log", log_level="INFO")
    # l.info("tst")
    #
    # logger.clear_log()
    # logger.close_log()
    # print(l.has_open_handlers())
    # print(logger.has_open_handlers())
    #
    # l.delete_log()
    # l.close_log()
    # print(l.has_open_handlers())







