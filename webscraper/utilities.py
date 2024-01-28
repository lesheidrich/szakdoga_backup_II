import random
import re
import time
from fake_user_agent import user_agent
from selenium.webdriver import ActionChains
from webscraper.proxy.proxy_handler import ProxyHandler
from typing import Optional, Callable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from requests.exceptions import RequestException


class WebKit:
    @staticmethod
    def new_header() -> dict:
        user = user_agent()
        return {'user-agent': user}

    @staticmethod
    def random_delay(min_sec: float = 1.0, max_sec: float = 5.0) -> None:
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)

    @staticmethod
    def move_mouse_to_element(driver: webdriver, element_xpath: str) -> None:
        first_div = driver.find_element(By.XPATH, element_xpath)
        action_chains = ActionChains(driver)
        action_chains.move_to_element(first_div).perform()

    @staticmethod
    def move_mouse(driver) -> None:
        try:
            WebKit.move_mouse_to_element(driver, '//body//div[1]')
        except NoSuchElementException:
            WebKit.move_mouse_to_element(driver, '//body')
        except Exception as e:
            raise ValueError(f"WebKit.move_mouse encountered an error running driver {driver}: {e}")


class ProxyKit:
    def __init__(self, proxies_csv: Optional[str], check_proxies: bool):
        self.proxy_list = self._initialize_proxy_list(proxies_csv, check_proxies)

    def _initialize_proxy_list(self, proxies_csv: Optional[str], check_proxies: bool) -> [str]:
        if proxies_csv is None:
            return []
        handler = ProxyHandler(proxies_csv)
        if check_proxies and proxies_csv.endswith("csv"):
            return handler.process_proxies()

        return handler.load_proxies()

    def pop_random_proxy(self) -> str | None:
        try:
            i = random.randint(0, len(self.proxy_list) - 1)
            return self.proxy_list.pop(i)
        except (IndexError, ValueError):
            return None

    @staticmethod
    def _load_proxy_str_to_dict(proxy_str: str) -> dict:
        return {
            'http': f"{proxy_str}",
            'https': f"{proxy_str}"
        }

    @staticmethod
    def is_valid_proxy(proxy_address: str) -> bool:
        proxy_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}:\d{1,5}$')
        if proxy_pattern.match(proxy_address):
            return True

        return False

    @staticmethod
    def proxy_to_dict(proxy: str) -> dict | None:
        if proxy and ProxyKit.is_valid_proxy(proxy):
            return ProxyKit._load_proxy_str_to_dict(proxy)

        return None

    def apply_rotating_proxy(self, function: Callable, url: str, *args, **kwargs):
        while True:
            proxy = self.pop_random_proxy()

            try:
                response = function(url, proxy, *args, **kwargs)
                if response.status_code == 200:
                    self.proxy_list.append(proxy)
                    return response
            except RequestException as e:
                print(f"ProxyKit.apply_rotating_proxy encountered an error while connecting to: {proxy}"
                      f" for {url}! {e}")
