import os
import re
from datetime import datetime

from log.logger import Logger
from scraper.proxy.proxy_handler import ProxyHandler
from secrets import PROJECT_FOLDER

if __name__ == "__main__":







    # h = ProxyHandler("proxies_test.csv")
    # working_proxy_list = h.process_proxies()


    """
    TODO:
    - integration test
    
    - webscraper
        - a) requests + bs4 + pd
        - b) requests + bs4
        - c) selenium + -> a & b
        - d) selenium only (maybe scrap)
        - unittest + integration test
    - scrapy
    - unittest + integration test
    
    
    
    
    Request structure
    try:
        print("requests")
        fail = 5/0
    except Exception:
        try:
            print("new proxy, del old one")
            print("scrapy")
            fail = 5 / 0
        except Exception:
            try:
                print("new proxy, del old one")
                print("selenium")
                fail = 5 / 0
            except Exception:
                try:
                    print("new proxy, del old one")
                    print("pyppeteer") <--cypress uses this
                    from pyppeteer import launch

                    async def main():
                        browser = await launch()
                        page = await browser.newPage()
                        await page.goto('http://example.com')
                        content = await page.content()
                        print(content)
                        await browser.close()
                    
                    # Run the event loop
                    import asyncio
                    asyncio.get_event_loop().run_until_complete(main())
                    
                    fail = 5 / 0
                except Exception:
                    print("can't get response")
    
    
    
    - sql alchemy db handler
    - unittest + integration test
    
    - clean up linter -> make into unittest, subtest for each dir, error if not 10
    - clean up regression + folders to exclude from linter
    
    - take PROJECT_FOLDER out of secrets.py -> setup.py
    
    ***TESTRUNNER
    unittest.TextTestRunner().run(suite)
    should be able to run tests and integrate with logger
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







