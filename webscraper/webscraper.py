from typing import Optional

import requests

from webscraper.request_service import RequestManager
from webscraper.selenium_service import WebDriverFactory
from webscraper.utilities import ProxyKit


class ScraperFacade:
    def __init__(self, proxies_csv: Optional[str] = "proxies_full.csv", check_proxies: bool = False):
        self.proxy_kit = ProxyKit(proxies_csv, check_proxies)

    def firefox_selenium_scrape(self, url: str, proxy=None):
        firefox = WebDriverFactory().firefox()
        return firefox.return_content(url, proxy)

    def chrome_selenium_scrape(self, url: str, proxy=None):
        chrome = WebDriverFactory().firefox()
        return chrome.return_content(url, proxy)

    def undetected_chrome_selenium_scrape(self, url: str, proxy=None):
        uc = WebDriverFactory().firefox()
        return uc.return_content(url, proxy)

    def firefox_selenium_scrape_proxy(self):
        pass

    def chrome_selenium_scrape_proxy(self):
        pass

    def undetected_chrome_selenium_scrape_proxy(self):
        pass

    def request_scrape(self, url: str, proxy: str = None, timeout=120) -> requests.Response:
        return RequestManager.request_response(url, proxy, timeout)

    def request_scrape_proxy(self, url: str):
        return self.proxy_kit.apply_rotating_proxy(RequestManager.request_response, url)
