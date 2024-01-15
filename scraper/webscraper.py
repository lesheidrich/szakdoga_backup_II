import random
import requests
import time

from fake_user_agent import user_agent
from scraper.proxy.proxy_handler import ProxyHandler
from typing import Literal


class WebScraper:
    def __init__(self):
        self.session = self.start_session()
        self.header = self.new_header()
        self.proxies = ["103.83.232.122:80", "122.155.165.191:3128"]
        self.current_proxy = ""

    def __del__(self):
        self.close_session()

    def new_header(self) -> dict:
        user = user_agent()
        return {'user-agent': user}

    def start_session(self) -> requests.Session:
        return requests.Session()

    def close_session(self) -> None:
        self.session.close()

    def random_delay(self, min_sec: float = 1.0, max_sec: float = 5.0) -> None:
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)

    def update_proxies(self):
        handler = ProxyHandler()
        self.proxies = handler.process_proxies()

    def new_proxy(self):
        try:
            self.current_proxy = random.choice(self.proxies)
            return {
                'http': f"{self.current_proxy}",
                'https': f"{self.current_proxy}"
            }
        except IndexError as e:
            return None

    def request_sauce(self, url: str, req_type: Literal["text", "content"], session=None) -> str:
        while True:
            try:
                if session:
                    response = session.get(
                        url, headers=self.new_header(), proxies=self.new_proxy())
                else:
                    response = requests.get(
                        url, headers=self.new_header(), proxies=self.new_proxy())

                return getattr(response, req_type)
            except OSError as e:
                print(f"{self.current_proxy} failed to connect. Regenerating request with new proxy.")
                self.proxies.remove(self.current_proxy)


