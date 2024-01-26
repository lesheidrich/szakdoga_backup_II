import random
import re
import requests
import time
from fake_user_agent import user_agent
from requests import HTTPError
from requests.exceptions import ProxyError
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from log.logger import Logger
from webscraper.proxy.proxy_handler import ProxyHandler
from typing import Literal

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import undetected_chromedriver as uc


# from webdriver_manager.chrome import ChromeDriverManager


class Toolkit:
    def new_header(self) -> dict:
        user = user_agent()
        return {'user-agent': user}

    def new_proxy_list(self, csv_file_name: str) -> [str]:
        handler = ProxyHandler(csv_file_name)
        return handler.process_proxies()

    def proxy_str_to_dict(self, proxy_str: str) -> dict:
        return {
            'http': f"{proxy_str}",
            'https': f"{proxy_str}"
        }

    def is_str_proxy(self, proxy_address: str) -> bool:
        proxy_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}:\d{1,5}$')
        if proxy_pattern.match(proxy_address):
            return True

        return False

    def random_delay(self, min_sec: float = 1.0, max_sec: float = 5.0) -> None:
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)


# class SeleniumManager:
#     def __init__(self):
#         self.kit = Toolkit()
#         self.driver = None
#         # self.initialize_new_driver()
#
#     def initialize_new_driver(self, browser: str = "chrome", proxy_address: str = None, headless: bool = False) -> None:
#         if browser == "chrome":
#             self._setup_chrome_driver(proxy_address, headless)
#         elif browser == "firefox":
#             self._setup_firefox_driver(proxy_address, headless)
#
#     def _setup_chrome_driver(self, proxy_address: str = None, headless: bool = False) -> None:
#         driver_options = uc.ChromeOptions()
#         # driver_options.headless = True
#         # driver_options.add_argument('--headless')
#
#         driver_options.add_argument('--proxy-server=%s' % proxy_address)
#
#         # driver_options.add_argument('--disable-extensions')
#         # driver_options.add_argument('--disable-notifications')
#         # driver_options.add_argument('--no-sandbox')
#         # driver_options.add_argument('--disable-dev-shm-usage')
#         # driver_options.add_argument('--disable-gpu')
#         # driver_options.add_argument('--mute-audio')
#         # driver_options.add_argument('--ignore-certificate-errors')
#         # driver_options.add_argument('--disable-logging')
#         driver = uc.Chrome(options=driver_options)
#
#         # driver_options.add_argument(f"--header={self.kit.new_header()}")
#         # if proxy_address is not None:
#         #     driver_options.add_argument(f'--proxy-server={proxy_address}')
#         # if headless and proxy_address is None:
#         #     driver_options.add_argument('--headless')
#         #     driver_options.add_argument('--disable-gpu')
#
#         # self.driver = webdriver.Chrome(options=driver_options)
#         self.driver = driver
#
#     def _setup_firefox_driver(self, proxy_address: str = None, headless: bool = False) -> None:
#         driver_options = Options()
#         driver_options.set_preference("general.useragent.override", self.kit.new_header()['user-agent'])
#         if proxy_address is not None:
#             # driver_options.set_preference("network.proxy.type", 1)
#             # driver_options.set_preference("network.proxy.http", proxy_address.split(":")[0])
#             # driver_options.set_preference("network.proxy.http_port", int(proxy_address.split(":")[1]))
#             # driver_options.set_preference("network.proxy.ssl", proxy_address.split(":")[0])
#             # driver_options.set_preference("network.proxy.ssl_port", int(proxy_address.split(":")[1]))
#             # # driver_options.update_preferences()  # might be deprecated
#
#             # HTTP proxy
#             driver_options.set_preference("network.proxy.type", 1)
#             driver_options.set_preference("network.proxy.http", proxy_address.split(":")[0])
#             driver_options.set_preference("network.proxy.http_port", int(proxy_address.split(":")[1]))
#
#             # SSL proxy
#             driver_options.set_preference("network.proxy.ssl", proxy_address.split(":")[0])
#             driver_options.set_preference("network.proxy.ssl_port", int(proxy_address.split(":")[1]))
#
#             # # FTP proxy (if needed)
#             # driver_options.set_preference("network.proxy.ftp", proxy_address.split(":")[0])
#             # driver_options.set_preference("network.proxy.ftp_port", int(proxy_address.split(":")[1]))
#
#         if headless:
#             driver_options.add_argument("--headless")
#
#         # driver_options.set_preference("dom.webdriver.enabled", False) # these should work just look into it
#         # driver_options.set_preference('useAutomationExtension', False)
#
#         self.driver = webdriver.Firefox(options=driver_options)
#
#     def get_html_text(self, url) -> str:
#         self.driver.get(url)
#         wait = WebDriverWait(self.driver, 90)  # Set the maximum waiting time to 90 seconds or more
#
#         try:
#             wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
#             self.move_mouse_to_first_div(self.driver)
#             html_content = self.driver.page_source
#         except Exception as e:
#             print(f"An error occurred: {e}")
#         finally:
#             self.driver.quit()
#             return html_content
#
#     def move_mouse_to_first_div(self, driver):
#         first_div = driver.find_element(By.XPATH, '//body//div[1]')
#         # Move the mouse to the first div
#         action_chains = webdriver.ActionChains(driver)
#         action_chains.move_to_element(first_div).perform()


class RequestManager:
    def __init__(self, proxy_choice: str | None = "proxies_full.csv", log_name_decorator: str = ""):
        self.kit = Toolkit()
        self.proxy_list = []
        self.proxy_as_dict = None
        self._setup_proxies(proxy_choice)

    def _setup_proxies(self, proxy_choice) -> None:
        if proxy_choice is not None and proxy_choice.endswith(".csv"):
            self.proxy_list = self.kit.new_proxy_list(proxy_choice)
            self.proxy_list = [self.kit.proxy_str_to_dict(proxy_str) for proxy_str in self.proxy_list]

    def _pop_proxy(self) -> None:
        try:
            i = random.randint(0, len(self.proxy_list) - 1)
            proxy = self.proxy_list.pop(i)
        except IndexError:
            proxy = None
        except ValueError:
            proxy = None

        self.proxy_as_dict = proxy

    def request_response(self, url: str) -> requests.Response:
        header = self.kit.new_header()
        response = requests.get(url, headers=header, proxies=self.proxy_as_dict)
        self.kit.random_delay()
        return response

    def request_response_proxy(self, url: str) -> None:
        while True:
            self._pop_proxy()
            try:
                response = self.request_response(url)
                print(self.proxy_as_dict)
                print(response.text)
                if response.status_code == 200:
                    self.proxy_list.append(self.proxy_as_dict)

                    return response
            except (ProxyError, ConnectionError) as e:
                print(self.proxy_as_dict, " couldn't connect!")
                print("on to the next one..")

    def selenium_save_html(self, url: str, new_proxy_address):
        # new_proxy_address = self.proxy
        self.selenium_manager.initialize_new_driver(browser="firefox",
                                                    proxy_address=new_proxy_address,
                                                    headless=True)
        # WebDriverException for proxy error
        return self.selenium_manager.get_html_text(url)





# ERRORS*******************************************************************************

# class HttpRequestError(Exception):
#     def __init__(self, response):
#         print("initializing")
#         self.response = response
#         self.message = f"Request to {self.response.url} failed!" \
#                        f"\n- status code: {self.response.status_code} " \
#                        f"\n- time elapsed: {self.response.elapsed}" \
#                        f"\n- response header: {self.response.headers}"
#         super().__init__(self.message)
#
#     def __str__(self):
#         print("printing")
#         return self.message


# except HTTPError as e:
#     self.session_manager.log.error(f"HTTP Error! Request to {url} failed!"
#                                    f"\n- status code: {e.response.status_code} "
#                                    f"\n- time elapsed: {e.response.elapsed}"
#                                    f"\n- response header: {e.response.headers}"
#                                    f"\n- message: {e}")

"""
Client Errors (4xx):
********************
400 Bad Request: Indicates that the request could not be understood by the server.
raise ValueError(f"Bad Request: {response.status_code}")

401 Unauthorized: Indicates that the request requires user authentication.
raise PermissionError(f"Unauthorized: {response.status_code}")

403 Forbidden: Indicates that the server understood the request but refuses to authorize it.
raise PermissionError(f"Forbidden: {response.status_code}")

404 Not Found: Indicates that the server did not find the requested resource.
raise FileNotFoundError(f"Not Found: {response.status_code}")

Server Errors (5xx):
*******************
500 Internal Server Error: Indicates that the server has encountered a situation it doesn't know how to handle.
raise RuntimeError(f"Internal Server Error: {response.status_code}")

502 Bad Gateway: Indicates that a server, while acting as a gateway or proxy, received an invalid response from an inbound server.
raise RuntimeError(f"Bad Gateway: {response.status_code}")

503 Service Unavailable: Indicates that the server is not ready to handle the request.
raise RuntimeError(f"Service Unavailable: {response.status_code}")
"""

# class SessionManager:
#     def __init__(self, proxy: str | None, log_name_decorator: str):
#         self.kit = Toolkit()
#         self.log = Logger(log_file="application_log.log",
#                           name=f"WEBSCRAPER-REQUEST{log_name_decorator}",
#                           log_level="INFO")
#         self.proxy = proxy
#         self.proxy_list = []
#         self.session = None
#         self.initialize_and_load_session()
#
#     def __del__(self):
#         if self.session is not None:
#             self.close_session()
#
#     def new_emtpy_session(self) -> None:
#         self.session = requests.Session()
#
#     def close_session(self) -> None:
#         self.session.close()
#         self.log.close_log()
#
#     def new_session(self) -> None:
#         if self.session is not None:
#             self.close_session()
#         self.new_emtpy_session()
#
#     def update_log_name(self, new_decorator: str) -> None:
#         self.log.close_log()
#         self.log = Logger(log_file="application_log.log",
#                           name=f"WEBSCRAPER-REQUEST{new_decorator}",
#                           log_level="INFO")
#
#     def proxy_str_to_dict(self, proxy_str: str) -> dict:
#         return {
#             'http': f"{proxy_str}",
#             'https': f"{proxy_str}"
#         }
#
#     def set_next_proxy_to_session(self) -> None:
#         next_proxy = self.kit.next_proxy(self.proxy_list)
#         proxy_dict = self.proxy_str_to_dict(next_proxy)
#         self.session.proxies.update(proxy_dict)
#
#     def load_fixed_proxy(self, proxy_address: str) -> None:
#         if not self.kit.is_proxy_str(proxy_address):
#             raise ValueError(f"Invalid argument for param proxy_address:"
#                              f"\n{proxy_address}!"
#                              f"\nFormat should match ip:port")
#
#         proxy_dict = self.proxy_str_to_dict(proxy_address)
#         self.session.proxies.update(proxy_dict)
#
#     def setup_proxy(self) -> None:
#         if self.proxy is not None and self.proxy.endswith(".csv"):
#             self.proxy_list = self.kit.new_proxy_list(self.proxy)
#             if self.proxy_list:
#                 self.set_next_proxy_to_session()
#         elif self.proxy is not None:
#             self.load_fixed_proxy(self.proxy)
#
#     def initialize_and_load_session(self) -> None:
#         self.new_session()
#         self.session.headers.update(self.kit.new_header())
#         self.setup_proxy()
#
#         self.log.info("SESSION REQUEST INITIALIZED:\n" +
#                       f"\theaders: {self.session.headers}\n" +
#                       f"\tproxies: {self.session.proxies}\n" +
#                       f"\tcookies: {self.session.cookies}\n" +
#                       f"\tclient side SSL cert: {self.session.cert}\n" +
#                       f"\tcan't be used to disable SSL certificate checks: {self.session.verify}\n" +
#                       f"\tadditional URL query params: {self.session.params}\n")
#
#     def new_session_info(self, new_log_decorator: str = "") -> None:
#         self.close_session()
#         self.update_log_name(new_log_decorator)
#         self.initialize_and_load_session()
