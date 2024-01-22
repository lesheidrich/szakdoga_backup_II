import random
import re
import requests
import time
from fake_user_agent import user_agent
from scraper.proxy.proxy_handler import ProxyHandler
from typing import Literal

"""
toolskit
    - new header
    - random delay
    - generate proxy list
    - next proxy in proxy list
    - selenium.move_mouse

setup / request setup
    - reqest setup
        - add header -> session.headers.update(self.new_header())
        - add proxy -> if proxy:
                          session.proxies.update(a)
                          session.proxies.update({'http': proxy, 'https': proxy})

content/result provider
    - request.get
    - selenium.savehtml
    
parse -> scrapeservice -> bs4 get all the shit from website and put it together into df
                          (maybe with DTO)
"""

# add log and log error as well
# put get number of pages here as well (unless there's a way to build it into it)

# def new_proxy(self):
#     try:
#         try:  # get next proxy
#             l = [5]
#             print(l.pop(0))
#             print(l)
#         except IndexError:
#             print(None)
#         return {  # load next proxy
#             'http': f"{self.current_proxy}",
#             'https': f"{self.current_proxy}"
#         }
#     except IndexError as e:
#         return None


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

    def move_mouse(self) -> None:
        pass


class SessionManager:
    def __init__(self, proxy: str | None):
        self.kit = Toolkit()
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

    def new_session(self) -> None:
        if self.session is not None:
            self.close_session()
        self.new_emtpy_session()

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

    def new_session_info(self) -> None:
        self.session.headers.update(self.kit.new_header())
        self.set_next_proxy_to_session()


class ContentProvider:
    def __init__(self, proxy: str | None = "proxies_full.csv"):
        self.session_manager = SessionManager(proxy)

    def request_sauce(self, url: str, session: requests.Session, req_type: Literal["text", "content"]) -> str:
        try:
            response = session.get(url)
            return getattr(response, req_type)
        except OSError as e:
            print(f"Failed to connect to proxy. {e}")

    def selenium_save_html(self):
        pass










