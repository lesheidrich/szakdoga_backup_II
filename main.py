import os
import re
from datetime import datetime
from log.logger import Logger
from webscraper.proxy.proxy_handler import ProxyHandler
from webscraper.request_service import ContentProvider
from secrets import PROJECT_FOLDER

if __name__ == "__main__":


    ip1 = "192.168.0.1:02"
    ip2 = "not_an_ip_address"

    cp = ContentProvider("proxies_test.csv")
    sm = cp.session_manager
    ses = sm.session

    print(ses.proxies)
    print(ses.headers)
    print(ses.cookies)

    for i in range(len(sm.proxy_list) + 2):
        print("Round: ", i+1)

        sm.new_session_info()

        ses.cookies = None
        ses.params = {}

        print(ses.proxies)
        print(ses.headers)
        print(ses.cookies)
        print(ses.verify)
        print(ses.cert)
        print(ses.params, "\n")



    # h = ProxyHandler("proxies_test.csv")
    # working_proxy_list = h.process_proxies()

    """
    Method/Attribute	Description	Notes
session.headers	Headers for HTTP requests.	Websites may use headers for user-agent identification.
session.cookies	Cookies associated with the session.	Used for session management and tracking user behavior.
session.auth	Authentication tuple (username, password).	Used for HTTP basic authentication.
session.proxies	Proxy configuration for requests.	May be used to hide the client's IP address.
session.verify	SSL certificate verification.	If False, may be used to disable SSL certificate checks.
session.cert	Client-side SSL certificate.	Used for mutual SSL authentication.
session.timeout	Timeout for requests.	Determines how long the client will wait for a response.
session.params	URL query parameters.	Additional parameters appended to the URL.
session.get()	Perform a GET request.	Initiates a GET request to the specified URL.
session.post()	Perform a POST request.	Initiates a POST request to the specified URL.
session.put()	Perform a PUT request.	Initiates a PUT request to the specified URL.
session.delete()	Perform a DELETE request.	Initiates a DELETE request to the specified URL.
session.request()	Generic HTTP request method.	Provides flexibility for making various HTTP requests.
session.prepare_request()	Prepares a request for sending.	Allows modification of a request before sending.
session.send()	Sends a prepared request.	Executes the prepared request and returns a response.
session.close()	Close the underlying connection.	Should be called to release resources when done.
    """

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
