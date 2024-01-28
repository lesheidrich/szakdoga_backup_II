from abc import ABC, abstractmethod
from typing import Optional
from selenium.webdriver import Firefox, FirefoxProfile, FirefoxOptions, ChromeOptions, Chrome
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webscraper.utilities import WebKit


class WebDriver(ABC):
    @abstractmethod
    def _setup_options(self) -> Options:
        pass

    @abstractmethod
    def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> None:
        pass

    @abstractmethod
    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        pass

    def _scrape_page_source(self, driver, url):
        driver.get(url)
        wait = WebDriverWait(driver, 90)  # Set the maximum waiting time to 90 seconds or more
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        WebKit.move_mouse(driver)
        # WebKit.random_delay()
        return driver.page_source

    def _return_and_quit(self, driver, url: str):
        try:
            return self._scrape_page_source(driver, url)
        except Exception as e:
            raise ConnectionError(f"WebDriver._scrape_page_source encountered an error while "
                                  f"attempting to scrape {url} with {driver}: {e}")
        finally:
            if driver:
                driver.quit()


class FirefoxDriver(WebDriver):
    def _setup_options(self) -> FirefoxOptions:
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("general.useragent.override", WebKit.new_header()['user-agent'])
        firefox_options.set_preference("dom.webdriver.enabled", False)
        firefox_options.set_preference('useAutomationExtension', False)
        firefox_options.add_argument("--headless")
        return firefox_options

    def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> None:
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 1)
        firefox_profile.set_preference("network.proxy.http", proxy_address.split(":")[0])
        firefox_profile.set_preference("network.proxy.http_port", int(proxy_address.split(":")[1]))
        firefox_profile.set_preference("network.proxy.ssl", proxy_address.split(":")[0])
        firefox_profile.set_preference("network.proxy.ssl_port", int(proxy_address.split(":")[1]))
        options.profile = firefox_profile

    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        firefox_options = self._setup_options()
        if proxy_address:
            self._setup_proxy(firefox_options, proxy_address)
        firefox_driver = Firefox(options=firefox_options)
        return self._return_and_quit(firefox_driver, url)


class ChromeDriver(WebDriver):
    def _setup_options(self) -> ChromeOptions:
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f"--header={WebKit.new_header()}")
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--mute-audio')
        chrome_options.add_argument('--ignore-certificate-errors')
        return chrome_options

    def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> None:
        if proxy_address:
            options.add_argument('--proxy-server=%s' % proxy_address)

    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        chrome_options = self._setup_options()
        self._setup_proxy(chrome_options, proxy_address)
        chrome_driver = Chrome(options=chrome_options)
        return self._return_and_quit(chrome_driver, url)


class UndetectedChromeDriver(WebDriver):
    def _setup_options(self) -> ChromeOptions:
        uc_options = uc.ChromeOptions()
        uc_options.headless = True
        uc_options.add_argument('--blink-settings=imagesEnabled=false')
        return uc_options

    def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> dict:
        return {'proxy': {'http': f'http://{proxy_address}',
                          'https': f'https://{proxy_address}'}}

    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        uc_options = self._setup_options()
        if proxy_address:
            proxy_options = self._setup_proxy(uc_options, proxy_address)
            uc_driver = uc.Chrome(options=uc_options, seleniumwire_options=proxy_options)
        else:
            uc_driver = uc.Chrome(options=uc_options)

        return self._return_and_quit(uc_driver, url)


class WebDriverFactory:
    @staticmethod
    def firefox() -> WebDriver:
        return FirefoxDriver()

    @staticmethod
    def chrome() -> WebDriver:
        return ChromeDriver()

    @staticmethod
    def undetected_chrome() -> WebDriver:
        return UndetectedChromeDriver()
