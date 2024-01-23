import os
import platform
import re
import subprocess
from datetime import datetime
from pprint import pprint

from log.logger import Logger
from webscraper.proxy.proxy_handler import ProxyHandler
from webscraper.request_service import ContentProvider
from secrets import PROJECT_FOLDER

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    url = "https://pythonprogramming.net/parsememcparseface/"
    urlb = "https://basketball.realgm.com/nba/teams/Boston-Celtics/2/individual-games/2006/points/Regular_Season/desc/7"





    # # MIGHT WORK FOR ALL OS - INSTALL FIREFOX
    # import os
    # import platform
    # import subprocess
    # import urllib.request
    #
    #
    # def is_firefox_installed():
    #     try:
    #         subprocess.run(["where", "firefox"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         return True
    #     except subprocess.CalledProcessError:
    #         return False
    #
    #
    # def install_firefox():
    #     try:
    #         system = platform.system().lower()
    #         if system == "linux":
    #             # Use the appropriate package manager command for your system
    #             # For example, on Ubuntu/Debian-based systems:
    #             subprocess.run(["sudo", "apt-get", "install", "firefox", "-y"], check=True)
    #
    #         elif system == "darwin":
    #             # Use Homebrew to install Firefox on macOS
    #             subprocess.run(["brew", "install", "firefox"], check=True)
    #
    #         elif system == "windows":
    #             # Download the Firefox installer
    #             url = "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US"
    #             installer_path = "firefox_installer.exe"
    #
    #             urllib.request.urlretrieve(url, installer_path)
    #
    #             # Run the installer silently
    #             subprocess.run([installer_path, "/S"], check=True)
    #
    #             # Clean up the installer
    #             os.remove(installer_path)
    #
    #         else:
    #             print(f"Unsupported operating system: {system}")
    #             return
    #
    #         print("Firefox installed successfully.")
    #     except subprocess.CalledProcessError as e:
    #         print(f"Failed to install Firefox: {e}")
    #
    #
    # if __name__ == "__main__":
    #     if not is_firefox_installed():
    #         install_firefox()
    #     else:
    #         print("Firefox is already installed.")











    # #CHECK WHICH OS
    # def get_operating_system():
    #     system = platform.system()
    #     return system.lower()
    #
    # os_type = get_operating_system()
    # if os_type == "linux" or os_type == "darwin":
    #     print("Running on Linux or macOS")
    #     # Your Linux/macOS-specific code here
    # elif os_type == "windows":
    #     print("Running on Windows")
    #     # Your Windows-specific code here
    # else:
    #     print(f"Unsupported operating system: {os_type}")



    # INSTALL FOR LINUX
    # import sh
    # def install_firefox():
    #     try:
    #         # Use the appropriate package manager command for your system
    #         # For example, on Ubuntu/Debian-based systems:
    #         sh.sudo("apt-get", "install", "firefox", "-y")
    #         print("Firefox installed successfully.")
    #     except sh.ErrorReturnCode as e:
    #         print(f"Failed to install Firefox: {e}")
    #
    # if not is_firefox_installed():
    #     install_firefox()
    # else:
    #     print("Firefox is already installed.")


    ## INSTALL FOR MAC
    # import sh
    # import platform
    # def is_firefox_installed():
    #     try:
    #         sh.which("firefox")
    #         return True
    #     except sh.ErrorReturnCode_1:
    #         return False
    # def install_firefox():
    #     try:
    #         system = platform.system().lower()
    #         if system == "darwin":
    #             # Use Homebrew to install Firefox on macOS
    #             sh.brew("install", "firefox")
    #         elif system == "linux":
    #             # Use the appropriate package manager command for your Linux distribution
    #             # For example, on Ubuntu/Debian-based systems:
    #             sh.sudo("apt-get", "install", "firefox", "-y")
    #         else:
    #             print(f"Unsupported operating system: {system}")
    #             return
    #
    #         print("Firefox installed successfully.")
    #     except sh.ErrorReturnCode as e:
    #         print(f"Failed to install Firefox: {e}")
    #
    # if not is_firefox_installed():
    #     install_firefox()
    # else:
    #     print("Firefox is already installed.")






    # # WIN INSTALL LINUX
    # import os
    # import platform
    # import subprocess
    # import urllib.request
    # def is_firefox_installed():
    #     try:
    #         subprocess.run(["where", "firefox"], check=True)
    #         return True
    #     except subprocess.CalledProcessError:
    #         return False
    # def install_firefox():
    #     try:
    #         system = platform.system().lower()
    #         if system == "windows":
    #             # Download the Firefox installer
    #             url = "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US"
    #             installer_path = "firefox_installer.exe"
    #
    #             urllib.request.urlretrieve(url, installer_path)
    #
    #             # Run the installer
    #             subprocess.run([installer_path], check=True)
    #
    #             # Clean up the installer
    #             os.remove(installer_path)
    #
    #         else:
    #             print(f"Unsupported operating system: {system}")
    #             return
    #
    #         print("Firefox installed successfully.")
    #     except subprocess.CalledProcessError as e:
    #         print(f"Failed to install Firefox: {e}")
    #
    # if not is_firefox_installed():
    #     install_firefox()
    # else:
    #     print("Firefox is already installed.")










    # # Create a new instance of the Firefox driver
    # driver = webdriver.Firefox()
    # print("navigating to page")
    #
    # # Navigate to the desired website
    # driver.get(urlb)
    # print("waiting")
    #
    # # Wait for the element with class 'tablesaw' to be present on the page
    # wait = WebDriverWait(driver, 90)  # Set the maximum waiting time to 90 seconds or more
    #
    # try:
    #     element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablesaw')))
    #     print("Element found, proceeding with further actions.")
    #
    #     # Now you can perform actions on the found element, if needed
    #
    # except Exception as e:
    #     print(f"Element not found within the specified time: {e}")
    #
    # print("Done waiting, grabbing content")
    #
    # # Get the HTML content of the current page
    # html_content = driver.page_source
    #
    # print("Grabbed content, gonna write now")
    #
    # # Save the HTML content to a file
    # with open("website.html", "w", encoding="utf-8") as file:
    #     file.write(html_content)
    #
    # print("Done writing")
    #
    # # Close the browser
    # driver.quit()












    # ip1 = "192.168.0.1:02"
    # ip2 = "not_an_ip_address"
    #
    # # cp = ContentProvider("proxies_test.csv")
    # # cp = ContentProvider(ip1)
    cp = ContentProvider(None)
    sm = cp.session_manager
    # sm_session = sm.session

    soup = cp.firefox_webdriver_save_html(urlb)
    # soup = cp.chrome_webdriver_save_html(urlb)
    # soup = cp.edge_webdriver_save_html(urlb)
    # soup = cp.safari_webdriver_save_html(urlb)
    # For edge and safari check the system and use the one that matches

    pprint(soup)

    # try:
    #     response = cp.request_sauce(url)
    # except Exception:
    #     print("puppyfarts")
    # # print(response.status_code)

    # pprint(response.headers)
    # pprint(response.headers['Server'])
    # pprint(response.url)
    # pprint(response.ok)
    # pprint(response.encoding)
    # pprint(response.elapsed)
    # pprint(response.cookies)
    # print(response.cookies.values())

    #there's already a fucking cookies.update method fucking use that

    # for i in range(len(sm.proxy_list) + 2):
    #     sm.new_session_info(f"-{i + 1}")
    #     response = cp.request_sauce(url)
    #     print(response.cookies.values()[0])


    # sm.update_cookies(response.cookies)






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

"""
REQUEST STRUCTURE


def dothedew(dodo):
    d = dodo.pop(0)
    print(d)
    # fail = 5 / 0


def runner(dl, func):

    while (len(dl) > 0):
        try:
            func(dl)
        except Exception:
            print("hoopsie")


if __name__ == "__main__":
    dolist = ["requests", "scrapy", "selenium", "pyppeteer"]

    runner(dolist, dothedew)
"""
