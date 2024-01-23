import random
import re
import requests
import time
from fake_user_agent import user_agent
from log.logger import Logger
from webscraper.proxy.proxy_handler import ProxyHandler
from typing import Literal

"""
content/result provider
    - request.get
    - selenium.savehtml
            -> move mouse in here
    
parse -> scrapeservice -> bs4 get all the shit from website and put it together into df
                          (maybe with DTO)
"""

# add log and log error as well
# put get number of pages here as well (unless there's a way to build it into it)


class Toolkit:
    def new_header(self) -> dict:
        user = user_agent()
        return {'user-agent': user}

    def new_proxy_list(self, csv_file_name: str) -> [str]:
        handler = ProxyHandler(csv_file_name)
        return handler.process_proxies()

    def next_proxy(self, proxy_list) -> str | None:
        try:
            return proxy_list.pop(0)
        except IndexError:
            return None

    def is_proxy_str(self, proxy_address: str) -> bool:
        proxy_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}:\d{1,5}$')
        if proxy_pattern.match(proxy_address):
            return True

        return False

    def random_delay(self, min_sec: float = 1.0, max_sec: float = 5.0) -> None:
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)


class SessionManager:
    def __init__(self, proxy: str | None, log_name_decorator: str):
        self.kit = Toolkit()
        self.log = Logger(log_file="application_log.log",
                          name=f"WEBSCRAPER-REQUEST{log_name_decorator}",
                          log_level="INFO")
        self.proxy = proxy
        self.proxy_list = []
        self.session = None
        self.initialize_and_load_session()

    def __del__(self):
        if self.session is not None:
            self.close_session()

    def new_emtpy_session(self) -> None:
        self.session = requests.Session()

    def close_session(self) -> None:
        self.session.close()
        self.log.close_log()

    def new_session(self) -> None:
        if self.session is not None:
            self.close_session()
        self.new_emtpy_session()

    def update_log_name(self, new_decorator: str) -> None:
        self.log.close_log()
        self.log = Logger(log_file="application_log.log",
                          name=f"WEBSCRAPER-REQUEST{new_decorator}",
                          log_level="INFO")

    def proxy_str_to_dict(self, proxy_str: str) -> dict:
        return {
            'http': f"{proxy_str}",
            'https': f"{proxy_str}"
            }

    def set_next_proxy_to_session(self) -> None:
        next_proxy = self.kit.next_proxy(self.proxy_list)
        proxy_dict = self.proxy_str_to_dict(next_proxy)
        self.session.proxies.update(proxy_dict)

    def load_fixed_proxy(self, proxy_address: str) -> None:
        if not self.kit.is_proxy_str(proxy_address):
            raise ValueError(f"Invalid argument for param proxy_address:"
                             f"\n{proxy_address}!"
                             f"\nFormat should match ip:port")

        proxy_dict = self.proxy_str_to_dict(proxy_address)
        self.session.proxies.update(proxy_dict)

    def setup_proxy(self) -> None:
        if self.proxy is not None and self.proxy.endswith(".csv"):
            self.proxy_list = self.kit.new_proxy_list(self.proxy)
            if self.proxy_list:
                self.set_next_proxy_to_session()
        elif self.proxy is not None:
            self.load_fixed_proxy(self.proxy)

    def initialize_and_load_session(self) -> None:
        self.new_session()
        self.session.headers.update(self.kit.new_header())
        self.setup_proxy()

        self.log.info("SESSION REQUEST INITIALIZED:\n" +
                      f"\theaders: {self.session.headers}\n" +
                      f"\tproxies: {self.session.proxies}\n" +
                      f"\tcookies: {self.session.cookies}\n" +
                      f"\tclient side SSL cert: {self.session.cert}\n" +
                      f"\tcan't be used to disable SSL certificate checks: {self.session.verify}\n" +
                      f"\tadditional URL query params: {self.session.params}\n")

    def new_session_info(self, new_log_decorator: str = "") -> None:
        self.session.headers.update(self.kit.new_header())
        self.set_next_proxy_to_session()
        self.session.cookies.clear()

        self.update_log_name(new_log_decorator)
        self.log.info("SESSION REQUEST RE-PARAMETERIZED:\n" +
                      f"\theaders: {self.session.headers}\n" +
                      f"\tproxies: {self.session.proxies}\n")


class HttpRequestError(Exception):
    def __init__(self, response):
        self.response = response
        self.message = f"Request to {self.response.url} failed!" \
                       f"\n- status code: {self.response.status_code} " \
                       f"\n- time elapsed: {self.response.elapsed}" \
                       f"\n- response header: {self.response.headers}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ContentProvider:
    def __init__(self, proxy: str | None = "proxies_full.csv", log_name_decorator: str = ""):
        self.session_manager = SessionManager(proxy, log_name_decorator)

    def request_sauce(self, url: str) -> requests.Response:
        # try:
        response = self.session_manager.session.get(url)
        response.raise_for_status()

        return response
        # except OSError as e:
        #     self.session_manager.log.warning(f"Failed to connect to proxy {self.session_manager.proxy}. {e}")

    def selenium_save_html(self):
        pass










