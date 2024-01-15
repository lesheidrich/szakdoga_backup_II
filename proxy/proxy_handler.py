"""
    h = ProxyHandler([Optional: path_to_your_proxy_list.csv])
    working_proxy_list = h.process_proxies()

    Maps proxy list to a request testing website to filter currently working
    proxies into a list.
    Default arg: proxy/proxy.csv.
"""

import requests
import csv
import multiprocessing
from log.logger import Logger


class ProxyHandler:
    log = Logger()

    def __init__(self, proxies_file: str = "proxy/proxy.csv"):
        self.proof_link = "http://icanhazip.com/"  # dummy website returns req ip
        self.proxies = self.load_proxies(proxies_file)

    def load_proxies(self, proxies_csv: str) -> [str]:
        """
        Allocates all proxies to a list of strings, concatenating ip:port
        :param proxies_csv: path to csv file containing proxies
        :return: list of proxy strings
        """
        with open(proxies_csv, "r") as file:
            return [f"{row[0]}:{row[1]}" for row in csv.reader(file)][1:]

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
            res = requests.get(self.proof_link, proxies=proxies, timeout=1)
            response_txt = res.text

            if res.status_code == 200 and 0 < len(response_txt) < 22:  # weed out html res to unset ubuntu servers
                self.log.info(
                    f"Proxy check succeeded\nIP: {proxy_address}\nStatus Code: {res.status_code}\nResponse: {response_txt}"
                )
                return proxy_address

        except requests.RequestException as e:
            self.log.warning(f"Proxy check failed for request {proxy_address}: {e}")

    def process_proxies(self) -> [str]:
        """
        Maps proxies to handle_proxy()
        :return: list of working proxy strings
        """
        self.log.info("COMMENCING PROXY LIST CHECK")
        with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
            result = list(filter(None, process.map(self.handle_proxy, self.proxies)))
            self.log.info("CURRENT WORKING PROXY LIST:\n" + "\n".join(result))
            self.log.close_log()
            return result
