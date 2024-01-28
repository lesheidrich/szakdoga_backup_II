from http.client import RemoteDisconnected
import requests
from requests.exceptions import (
    ProxyError,
    ConnectionError,
    Timeout,
    TooManyRedirects,
    InvalidURL,
    HTTPError,
    RequestException,
)
from urllib3.exceptions import ProtocolError
from typing import Callable
from webscraper.utilities import WebKit, ProxyKit


class RequestManager:
    @staticmethod
    def request_response(url: str, proxy: dict = None, timeout=1) -> requests.Response:
        header = WebKit.new_header()
        # WebKit.random_delay()
        proxy_dict = ProxyKit.proxy_to_dict(proxy)
        return requests.get(url, headers=header, proxies=proxy_dict, timeout=timeout)

    def request_response_rotating_proxy(self, url: str, timeout=120) -> requests.Response:
        while True:
            proxy = self.proxy_kit.pop_random_proxy()
            # proxy_dict = self.proxy_kit.proxy_to_dict(proxy)

            try:
                response = self.request_response(url, proxy, timeout)
                if response.status_code == 200:
                    self.proxy_kit.proxy_list.append(proxy)
                    return response
            # except (ProxyError, ConnectionError, Timeout, TooManyRedirects, InvalidURL, HTTPError,
            except RequestException as e:
                print(f"Error trying to connect to: {proxy} for {url}! {e}")

    def apply_rotating_proxy(func: Callable, proxy_kit, url: str, *args, **kwargs):
        while True:
            proxy = proxy_kit.pop_random_proxy()
            proxy_dict = proxy_kit.proxy_to_dict(proxy)

            try:
                response = func(url, proxy_dict, *args, **kwargs)
                if response.status_code == 200:
                    proxy_kit.proxy_list.append(proxy)
                    return response
            except RequestException as e:
                print(f"Error trying to connect to: {proxy} for {url}! {e}")

