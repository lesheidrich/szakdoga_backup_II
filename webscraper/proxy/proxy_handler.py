"""
Module: proxy_handler.py

This module defines the ProxyHandler class, which is responsible for mapping a proxy list to a request
testing website to filter currently working proxies into a list.

Usage Example:
--------------
h = ProxyHandler("path/to/your/proxy_list.csv")
working_proxy_list = h.process_proxies()

Input file specifications:
  - must be csv
  - assumes the first row is headers
  - first 2 columns must contain:
      1) ip address
      2) port number

Attributes:
-----------
- test_url (str): Dummy website URL that returns the requesting IP.
- log (Logger): Instance of Logger class for logging.
- file_path (str): Absolute path to the CSV file containing proxies.
- proxies (list): List of proxy strings loaded from the CSV file.

Methods:
--------
- __init__(self, proxies_file: str = "proxies_full.csv"):
    Initializes the ProxyHandler object.

- _build_path(self, file_name: str) -> str:
    Builds the absolute path to the CSV file. Returns the argument if already an absolute path.

- load_proxies(self) -> [str]:
    Loads proxies from the CSV file into a list of strings.

- handle_proxy(self, proxy_address: str) -> str:
    Sets an individual proxy IP:port as http/https to attempt a request.

- process_proxies(self) -> [str]:
    Maps proxies to handle_proxy() using multiprocessing.
"""
import csv
import multiprocessing
import os

import secrets
import requests
from log.logger import Logger


class ProxyHandler:
    """
    class: ProxyHandler
    h = ProxyHandler([Optional: path_to_your_proxy_list.csv])
    working_proxy_list = h.process_proxies()

    Maps proxy list to a request testing website to filter currently working
    proxies into a list.
    Default arg: proxy/proxies_full.csv.

    Input file specifications:
        - must be csv
        - assumes the first row is headers
        - first 2 columns must contain:
            1) ip address
            2) port number

    Usage Example:
    --------------
    h = ProxyHandler("path/to/your/proxy_list.csv")
    working_proxy_list = h.process_proxies()

    Attributes:
    -----------
    - test_url (str): Dummy website URL that returns the requesting IP.
    - log (Logger): Instance of Logger class for logging.
    - file_path (str): Absolute path to the CSV file containing proxies.
    - proxies (list): List of proxy strings loaded from the CSV file.

    Methods:
    --------
    - __init__(self, proxies_file: str = "proxies_full.csv"):
        Initializes the ProxyHandler object.

    - _build_path(self, file_name: str) -> str:
        Builds the absolute path to the CSV file. Returns the argument if already an absolute path.

    - load_proxies(self) -> [str]:
        Loads proxies from the CSV file into a list of strings.

    - handle_proxy(self, proxy_address: str) -> str:
        Sets an individual proxy IP:port as http/https to attempt a request.

    - process_proxies(self) -> [str]:
        Maps proxies to handle_proxy() using multiprocessing.

    """
    def __init__(self, proxies_file: str = "proxies_full.csv"):
        self.test_url = "http://icanhazip.com/"  # dummy website returns req ip
        self.log = Logger(log_file="application_log.log",
                          name="PROXY HANDLER",
                          log_level="DEBUG")
        self.file_path = self._build_path(proxies_file)
        self.proxies = self.load_proxies()

    def _build_path(self, file_name: str) -> str:
        """
        Builds absolute path to csv file. Returns arg if already absolute path.
        :param file_name: str name of csv file containing proxies
        :return: absolute file path str
        """
        if not file_name.endswith(".csv"):
            raise ValueError("Invalid input for proxy list filename. File must be csv!")

        if ":\\" in file_name:
            return file_name
        return os.path.join(secrets.get_project_folder(), "webscraper", "proxy", file_name)

    def load_proxies(self) -> [str]:
        """
        Allocates all proxies to a list of strings, concatenating ip:port
        :return: list of proxy strings
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            result = [f"{row[0]}:{row[1]}" for row in csv.reader(file)][1:]
        return result

    def handle_proxy(self, proxy_address: str) -> str:
        """
        Sets individual proxy ip:port as http/https to attempt a request
        :param proxy_address: str ip:port
        :return: str of proxy address ip:port upon successful response
        """
        proxies = {
            'http': f"http://{proxy_address}",
            'https': f"https://{proxy_address}"
        }

        try:
            res = requests.get(self.test_url, proxies=proxies, timeout=1)
            response_txt = res.text

            # if res.status_code == 200 and 0 < len(response_txt) < 22:
            if res.status_code == 200 and proxy_address.split(":")[0] in response_txt:
                # weed out html res to unset ubuntu servers
                self.log.info(
                    f"Proxy check succeeded\nIP: {proxy_address}\nStatus Code: {res.status_code}"
                    f"\nResponse: {response_txt}"
                )
                return proxy_address
        except requests.RequestException as e:
            self.log.warning(f"Proxy check failed for request {proxy_address}: {e}")

        return ""

    def process_proxies(self) -> [str]:
        """
        Maps proxies to handle_proxy()
        :return: list of working proxy strings
        """
        self.log.info(30*"*")
        self.log.info("COMMENCING PROXY LIST CHECK")
        with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
            result = list(filter(None, process.map(self.handle_proxy, self.proxies)))

        self.log.info("CURRENT WORKING PROXY LIST:\n" + "\n".join(result) + "\n")
        self.log.close_log()
        return result
