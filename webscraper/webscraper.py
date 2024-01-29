from typing import Optional
import requests
from webscraper.selenium_service import WebDriverFactory
from webscraper.utilities import ProxyKit, WebKit


class ScraperFacade:
    def __init__(self, proxies_csv: Optional[str] = "proxies_full.csv", check_proxies: bool = False):
        self.proxy_kit = ProxyKit(proxies_csv, check_proxies)

    def firefox_selenium_scrape(self, url: str, proxy=None):
        firefox = WebDriverFactory().firefox()
        WebKit.random_delay()
        return firefox.return_content(url, proxy)

    def firefox_selenium_scrape_proxy(self, url: str):
        return self.proxy_kit.apply_rotating_proxy(self.firefox_selenium_scrape, url)

    def chrome_selenium_scrape(self, url: str, proxy=None):
        chrome = WebDriverFactory().chrome()
        WebKit.random_delay()
        return chrome.return_content(url, proxy)

    def chrome_selenium_scrape_proxy(self, url: str):
        return self.proxy_kit.apply_rotating_proxy(self.chrome_selenium_scrape, url)

    def undetected_chrome_selenium_scrape(self, url: str, proxy=None):
        uc = WebDriverFactory().undetected_chrome()
        WebKit.random_delay()
        return uc.return_content(url, proxy)

    def undetected_chrome_selenium_scrape_proxy(self, url: str):
        return self.proxy_kit.apply_rotating_proxy(self.undetected_chrome_selenium_scrape, url)

    def requests_scrape(self, url: str, proxy: str = None, timeout=120) -> requests.Response:
        header = WebKit.new_header()
        proxy_dict = ProxyKit.proxy_to_dict(proxy)
        WebKit.random_delay()
        return requests.get(url, headers=header, proxies=proxy_dict, timeout=timeout)

    def requests_scrape_proxy(self, url: str):
        return self.proxy_kit.apply_rotating_proxy(self.requests_scrape, url)

    def scrapy_scrape(self, url: str):
        WebKit.random_delay()
        pass

    def scrapy_scrape_proxy(self, url: str):
        pass
