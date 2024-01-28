import multiprocessing
import time
from functools import partial
from pprint import pprint
from urllib import request

import requests

from webscraper.request_service import RequestManager, WebKit
from webscraper.selenium_service import WebDriverFactory
from webscraper.utilities import ProxyKit
from webscraper.webscraper import ScraperFacade

# Separate button for setup proxy list form csv, assume it's already done otherwise

# use_proxy = True/False <--radio button use proxy list provided <-- move to toolkit

scrape_method = "request_sauce"  # Literal["request", "scpy", "sel_firefox", "sel_uc"]
"""
scraper = getattr(request_service.cp, scrape_method)

url = "https://www.icanhazip.com"
s = "get"
funct = getattr(requests, s{proxy_choice+_})
response = funct(url)
print(response.text)
"""

team = "Boston-Celtics"  # Entire
bbalreferenceteam = "BOS"
year = "2006"
game_type = "Regular_Season"  # Literal["Regular_Season", "Playoffs"]
page_number = 1
stat_type = "Averages"  # Literal["Averages", "Totals", "Per_48", "Per_40", "Per_36", "Per_Minute", "Minute_Per", "Misc_Stats", "Advanced_Stats"]

links = [
    f"https://basketball.realgm.com/nba/teams/{team}/2/individual-games/{year}/points/{game_type}/desc/{page_number}",

    f"https://basketball.realgm.com/nba/teams/{team}/2/Stats/{year}/{stat_type}/All/points/All/desc/{page_number}/Away",
    f"https://basketball.realgm.com/nba/teams/{team}/2/Stats/{year}/{stat_type}/All/points/All/desc/{page_number}/Home",

    f"https://basketball.realgm.com/nba/teams/{team}/2/Depth_Charts",

    f"https://basketball.realgm.com/nba/team-stats/{year}/Advanced_Stats/Team_Totals/{game_type}",

    f"https://www.basketball-reference.com/teams/{bbalreferenceteam}/{year}.html"
]

"""
TODO:
    - read page: while <a> Next Page >></a> : page_number += 1 and recursively re-run
    
    https://basketball.realgm.com/nba/                       individual-games/2006/points/Playoffs/desc/1
    https://basketball.realgm.com/nba/teams/Boston-Celtics/2/individual-games/2006/points/Playoffs/desc/1
    
    use_proxy = yes/no
    
    cp(use_proxy)
        - if use proxy: setup proxy list
    sp.scrape_with_selected_strategy(proxy)
        - header: always
        - proxy: rotate always
            - proxy list
            - pop
            - to dict
        - random wait
        
        
        response.raise_for_status()
    
"""

# url = "https://basketball.realgm.com/nba/teams/Boston-Celtics/2/individual-games/2006/points/Playoffs/desc/1"
url = "https://www.icanhazip.com"

if __name__ == '__main__':

    content = """103.127.1.130	80	BD	Bangladesh	anonymous	no	no	9 secs ago
117.250.3.58	8080	IN	India	elite proxy	no	yes	9 secs ago
50.168.163.176	80	US	United States	anonymous	no	no	9 secs ago
50.174.145.10	80	US	United States	anonymous	no	no	9 secs ago
50.168.72.119	80	US	United States	anonymous	no	no	9 secs ago
50.174.41.66	80	US	United States	anonymous	no	no	9 secs ago
167.114.107.37	80	CA	Canada	elite proxy	no	yes	9 secs ago
50.239.72.19	80	US	United States	anonymous	no	no	9 secs ago
209.97.150.167	3128	US	United States	anonymous	no	no	9 secs ago
50.173.140.150	80	US	United States	anonymous	no	no	9 secs ago
50.173.140.146	80	US	United States	anonymous	no	no	9 secs ago
202.5.16.44	80	US	United States	anonymous	no	no	9 secs ago
39.109.113.97	3128	HK	Hong Kong	anonymous	no	no	9 secs ago
50.168.210.226	80	US	United States	anonymous	no	no	9 secs ago
96.113.158.126	80	US	United States	anonymous	no	no	9 secs ago
50.223.38.6	80	US	United States	anonymous	no	no	9 secs ago
50.174.145.13	80	US	United States	anonymous	no	no	9 secs ago
50.200.12.80	80	US	United States	anonymous	no	no	9 secs ago
50.222.245.40	80	US	United States	anonymous	no	no	9 secs ago
50.169.23.170	80	US	United States	anonymous	no	no	9 secs ago
198.44.255.3	80	HK	Hong Kong	anonymous	no	no	9 secs ago
50.172.75.126	80	US	United States	anonymous	no	no	9 secs ago
50.168.210.234	80	US	United States	anonymous	no	no	9 secs ago
50.168.210.236	80	US	United States	anonymous	no	no	9 secs ago
50.221.230.186	80	US	United States	anonymous	no	no	9 secs ago
50.171.68.130	80	US	United States	anonymous	no	no	9 secs ago
50.200.12.82	80	US	United States	anonymous	no	no	9 secs ago
50.171.152.30	80	US	United States	anonymous	no	no	9 secs ago
50.172.75.123	80	US	United States	anonymous	no	no	9 secs ago
50.222.245.47	80	US	United States	anonymous	no	no	9 secs ago
50.174.145.12	80	US	United States	anonymous	no	no	9 secs ago
50.173.140.149	80	US	United States	anonymous	no	no	9 secs ago
50.174.7.153	80	US	United States	anonymous	no	no	9 secs ago
50.206.111.88	80	US	United States	anonymous	no	no	9 secs ago
50.239.72.17	80	US	United States	anonymous	no	no	9 secs ago
50.174.7.152	80	US	United States	anonymous	no	no	9 secs ago
24.205.201.186	80	US	United States	anonymous	no	no	9 secs ago
50.220.168.134	80	US	United States	anonymous	no	no	9 secs ago
50.204.219.226	80	US	United States	anonymous	no	no	9 secs ago
50.173.140.144	80	US	United States	anonymous	no	no	9 secs ago
50.231.110.26	80	US	United States	anonymous	no	no	9 secs ago
68.188.59.198	80	US	United States	anonymous	no	no	9 secs ago
50.168.163.178	80	US	United States	anonymous	no	no	9 secs ago
50.206.111.91	80	US	United States	anonymous	no	no	9 secs ago
50.168.72.117	80	US	United States	anonymous	no	no	9 secs ago
50.206.111.90	80	US	United States	anonymous	no	no	9 secs ago
139.59.1.14	8080	IN	India	anonymous	no	no	9 secs ago
50.218.57.66	80	US	United States	anonymous	no	no	9 secs ago
47.88.3.19	8080	US	United States	anonymous	no	no	9 secs ago
50.218.57.70	80	US	United States	anonymous	no	no	9 secs ago
103.133.222.220	102	ID	Indonesia	anonymous	no	yes	9 secs ago
207.2.120.19	80	US	United States	anonymous	no	no	9 secs ago
50.204.219.228	80	US	United States	anonymous	no	no	9 secs ago
50.174.145.8	80	US	United States	anonymous	no	no	9 secs ago
50.173.140.148	80	US	United States	anonymous	no	no	9 secs ago
50.173.140.145	80	US	United States	anonymous	no	no	9 secs ago
213.33.126.130	80	AT	Austria	anonymous	no	no	9 secs ago
50.168.72.114	80	US	United States	anonymous	no	no	9 secs ago
50.207.199.85	80	US	United States	anonymous	no	no	9 secs ago
50.207.199.81	80	US	United States	anonymous	no	no	9 secs ago
50.170.90.28	80	US	United States	anonymous	no	no	9 secs ago
50.170.90.25	80	US	United States	anonymous	no	no	9 secs ago
50.170.90.30	80	US	United States	anonymous	no	no	9 secs ago
162.222.207.221	80	US	United States	elite proxy	yes	no	9 secs ago
50.170.90.24	80	US	United States	anonymous	no	no	9 secs ago
50.168.72.113	80	US	United States	anonymous	no	no	9 secs ago
123.30.154.171	7777	VN	Vietnam	anonymous	no	no	9 secs ago
20.24.43.214	80	SG	Singapore	elite proxy	no	no	9 secs ago
20.206.106.192	80	BR	Brazil	elite proxy	no	no	9 secs ago
80.150.50.226	80	DE	Germany	anonymous	no	no	9 secs ago
50.207.199.83	80	US	United States	anonymous	no	no	9 secs ago
50.204.219.227	80	US	United States	anonymous	no	no	9 secs ago
80.228.235.6	80	DE	Germany	anonymous	no	no	9 secs ago
50.239.72.16	80	US	United States	anonymous	no	no	9 secs ago
50.217.226.41	80	US	United States	anonymous	no	no	9 secs ago
96.113.159.162	80	US	United States	anonymous	no	no	9 secs ago
50.202.75.26	80	US	United States	anonymous	no	no	9 secs ago
50.217.226.44	80	US	United States	anonymous	no	no	9 secs ago
50.172.23.10	80	US	United States	anonymous	no	no	9 secs ago
50.169.135.10	80	US	United States	anonymous	no	no	9 secs ago
47.56.110.204	8989	HK	Hong Kong	anonymous	yes	no	9 secs ago
50.217.226.46	80	US	United States	anonymous	no	no	9 secs ago
127.0.0.7	80		Unknown	anonymous	no	no	9 secs ago
50.204.219.224	80	US	United States	anonymous	no	no	9 secs ago
20.205.61.143	80	HK	Hong Kong	elite proxy	no	no	9 secs ago
50.217.226.42	80	US	United States	anonymous	no	no	9 secs ago
50.174.7.159	80	US	United States	anonymous	no	no	9 secs ago
103.153.246.65	3125	ID	Indonesia	transparent	no	no	22 secs ago
185.100.215.44	3128	PL	Poland	transparent	no	no	27 secs ago
154.202.106.67	3128	US	United States	transparent	no	no	27 secs ago
34.87.84.105	80	SG	Singapore	transparent	no	no	27 secs ago
154.202.117.55	3128	US	United States	transparent	no	no	27 secs ago
154.202.104.53	3128	US	United States	transparent	no	no	27 secs ago
103.91.82.177	8080	IN	India	transparent	no	no	2 mins ago
45.174.248.19	999	MX	Mexico	transparent	no	no	2 mins ago
5.75.164.195	3128	DE	Germany	transparent	no	no	3 mins ago
107.155.65.11	3128	SG	Singapore	transparent	no	no	7 mins ago
103.155.166.92	8181	ID	Indonesia	transparent	no	no	7 mins ago
116.97.240.147	4995	VN	Vietnam	transparent	no	no	7 mins ago
167.249.30.64	999	CL	Chile	transparent	no	no	7 mins ago"""

    ip = []



    # print(response.text)

    rows = content.split("\n")
    for r in rows:
        tabs = r.split("\t")
        ip.append(tabs[0].strip() + ":" + tabs[1].strip())

    """
    INSTANCIATE AND RUN WEBDRIVER BASED ON PARAM INPUT
    fact = getattr(WebDriverFactory(), "firefox")
    func = fact()
    r = func.return_content(url)
    """

    sf = ScraperFacade(None)
    sf.proxy_kit.proxy_list = ip

    print(sf.proxy_kit.proxy_list)

    response = sf.request_scrape_proxy(url)

    print(response.text)


    # # response = c.return_content(url)
    # # print(response)
    #
    # while len(ip) > 0:
    #     try:
    #         proxy = ip.pop()
    #
    #         print(proxy, "***********************")
    #
    #         # result = sf.firefox_selenium_scrape(url)
    #         # print(result)
    #
    #         # response = rq.undetected_chrome_save_html(url, proxy)
    #         # print("Selenium Success:", proxy.split(":")[0].strip() in response)
    #         # pprint(response)
    #         #
    #         # p = kit.proxy_str_to_dict(proxy)
    #         # resp = rq.request_response(url, p)
    #         # print("Requests Success: ", proxy.split(":")[0].strip() in resp.text)
    #         # print(proxy, ": ", resp.text)
    #
    #
    #     except Exception as e:
    #         print("puppyfarts")
    #         print(e)

# if proxy=False then None, else grab proxy from csvtolist
# cp = ContentProvider(None)
# funct = getattr(cp, scrape_method)
#
# response = funct(url)
# print("176.63.13.165" in response.text)




# class SessionManager:
#     def __init__(self, proxy: str | None, log_name_decorator: str):
#         self.kit = Toolkit()
#         self.log = Logger(log_file="application_log.log",
#                           name=f"WEBSCRAPER-REQUEST{log_name_decorator}",
#                           log_level="INFO")
#         self.proxy = proxy
#         self.proxy_list = []
#         self.session = None
#         self.initialize_and_load_session()
#
#     def __del__(self):
#         if self.session is not None:
#             self.close_session()
#
#     def new_emtpy_session(self) -> None:
#         self.session = requests.Session()
#
#     def close_session(self) -> None:
#         self.session.close()
#         self.log.close_log()
#
#     def new_session(self) -> None:
#         if self.session is not None:
#             self.close_session()
#         self.new_emtpy_session()
#
#     def update_log_name(self, new_decorator: str) -> None:
#         self.log.close_log()
#         self.log = Logger(log_file="application_log.log",
#                           name=f"WEBSCRAPER-REQUEST{new_decorator}",
#                           log_level="INFO")
#
#     def proxy_str_to_dict(self, proxy_str: str) -> dict:
#         return {
#             'http': f"{proxy_str}",
#             'https': f"{proxy_str}"
#         }
#
#     def set_next_proxy_to_session(self) -> None:
#         next_proxy = self.kit.next_proxy(self.proxy_list)
#         proxy_dict = self.proxy_str_to_dict(next_proxy)
#         self.session.proxies.update(proxy_dict)
#
#     def load_fixed_proxy(self, proxy_address: str) -> None:
#         if not self.kit.is_proxy_str(proxy_address):
#             raise ValueError(f"Invalid argument for param proxy_address:"
#                              f"\n{proxy_address}!"
#                              f"\nFormat should match ip:port")
#
#         proxy_dict = self.proxy_str_to_dict(proxy_address)
#         self.session.proxies.update(proxy_dict)
#
#     def setup_proxy(self) -> None:
#         if self.proxy is not None and self.proxy.endswith(".csv"):
#             self.proxy_list = self.kit.new_proxy_list(self.proxy)
#             if self.proxy_list:
#                 self.set_next_proxy_to_session()
#         elif self.proxy is not None:
#             self.load_fixed_proxy(self.proxy)
#
#     def initialize_and_load_session(self) -> None:
#         self.new_session()
#         self.session.headers.update(self.kit.new_header())
#         self.setup_proxy()
#
#         self.log.info("SESSION REQUEST INITIALIZED:\n" +
#                       f"\theaders: {self.session.headers}\n" +
#                       f"\tproxies: {self.session.proxies}\n" +
#                       f"\tcookies: {self.session.cookies}\n" +
#                       f"\tclient side SSL cert: {self.session.cert}\n" +
#                       f"\tcan't be used to disable SSL certificate checks: {self.session.verify}\n" +
#                       f"\tadditional URL query params: {self.session.params}\n")
#
#     def new_session_info(self, new_log_decorator: str = "") -> None:
#         self.close_session()
#         self.update_log_name(new_log_decorator)
#         self.initialize_and_load_session()


# ERRORS*******************************************************************************

# class HttpRequestError(Exception):
#     def __init__(self, response):
#         print("initializing")
#         self.response = response
#         self.message = f"Request to {self.response.url} failed!" \
#                        f"\n- status code: {self.response.status_code} " \
#                        f"\n- time elapsed: {self.response.elapsed}" \
#                        f"\n- response header: {self.response.headers}"
#         super().__init__(self.message)
#
#     def __str__(self):
#         print("printing")
#         return self.message


# except HTTPError as e:
#     self.session_manager.log.error(f"HTTP Error! Request to {url} failed!"
#                                    f"\n- status code: {e.response.status_code} "
#                                    f"\n- time elapsed: {e.response.elapsed}"
#                                    f"\n- response header: {e.response.headers}"
#                                    f"\n- message: {e}")

"""
Client Errors (4xx):
********************
400 Bad Request: Indicates that the request could not be understood by the server.
raise ValueError(f"Bad Request: {response.status_code}")

401 Unauthorized: Indicates that the request requires user authentication.
raise PermissionError(f"Unauthorized: {response.status_code}")

403 Forbidden: Indicates that the server understood the request but refuses to authorize it.
raise PermissionError(f"Forbidden: {response.status_code}")

404 Not Found: Indicates that the server did not find the requested resource.
raise FileNotFoundError(f"Not Found: {response.status_code}")

Server Errors (5xx):
*******************
500 Internal Server Error: Indicates that the server has encountered a situation it doesn't know how to handle.
raise RuntimeError(f"Internal Server Error: {response.status_code}")

502 Bad Gateway: Indicates that a server, while acting as a gateway or proxy, received an invalid response from an inbound server.
raise RuntimeError(f"Bad Gateway: {response.status_code}")

503 Service Unavailable: Indicates that the server is not ready to handle the request.
raise RuntimeError(f"Service Unavailable: {response.status_code}")
"""