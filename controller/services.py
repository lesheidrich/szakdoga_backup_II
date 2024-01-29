import multiprocessing
import time
from functools import partial
from pprint import pprint
from urllib import request

import requests

from webscraper.parse_service import Parser
from webscraper.selenium_service import WebDriverFactory
from webscraper.utilities import ProxyKit
from webscraper.webscraper import ScraperFacade

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
    
    # entire nba
    https://basketball.realgm.com/nba/                       individual-games/2006/points/Playoffs/desc/1  
    https://basketball.realgm.com/nba/teams/Boston-Celtics/2/individual-games/2006/points/Playoffs/desc/1
    
    - Separate button for setup proxy list form csv, assume it's already done otherwise
    - use_proxy = True/False <--radio button use proxy list provided <-- move to toolkit
    
    sf = ScraperFacade(None)
    m = "firefox_selenium_scrape"
    funct = getattr(sf, m)
    print(funct(url))
    
    m = "requests_scrape"
    funct = getattr(sf, m)
    print(funct(url).text)
"""

# url = "https://basketball.realgm.com/nba/teams/Boston-Celtics/2/individual-games/2006/points/Playoffs/desc/1"
url = "https://www.icanhazip.com"

if __name__ == '__main__':

    path = "C:\\Downloads\\html_tmp\\a.html"
    with open(path, "r") as file:
        df = Parser.html_table_2_df(file)

    print(df)

#     # IP ADDRESSES
#     content = """188.235.0.207	8181	RU	Russian Federation	anonymous	yes	no	2 secs ago
# 51.210.216.54	80	FR	France	elite proxy	yes	no	2 secs ago
# 45.56.119.212	8015	US	United States	anonymous	yes	no	2 secs ago
# 5.78.41.117	8080	US	United States	anonymous	yes	no	2 secs ago
# 143.110.232.177	80	US	United States	elite proxy	yes	no	15 secs ago
# 13.81.217.201	80	NL	Netherlands	elite proxy	no	no	15 secs ago
# 218.255.187.60	80	HK	Hong Kong	elite proxy	no	no	15 secs ago
# 51.250.13.88	80	RU	Russian Federation	elite proxy	no	no	15 secs ago
# 178.128.200.87	80	DE	Germany	elite proxy	no	no	15 secs ago
# 20.210.113.32	80	JP	Japan	elite proxy	no	no	15 secs ago
# 102.130.125.86	80	ZA	South Africa	elite proxy	yes	no	15 secs ago
# 156.67.214.232	80	SG	Singapore	elite proxy	no	no	15 secs ago
# 174.138.94.117	80	US	United States	elite proxy	yes	no	15 secs ago
# 50.174.145.14	80	US	United States	anonymous	no	no	15 secs ago
# 50.168.210.238	80	US	United States	anonymous	no	no	15 secs ago
# 41.204.63.118	80	GH	Ghana	elite proxy	yes	no	15 secs ago
# 200.19.177.120	80	BR	Brazil	elite proxy	yes	no	15 secs ago
# 74.48.78.52	80	US	United States	elite proxy	yes	no	15 secs ago
# 194.182.187.78	3128	AT	Austria	anonymous	no	no	15 secs ago
# 159.65.77.168	8585	US	United States	anonymous	no	no	15 secs ago
# 50.168.72.122	80	US	United States	anonymous	no	no	15 secs ago
# 154.57.7.36	80	GR	Greece	elite proxy	yes	no	15 secs ago
# 50.170.90.26	80	US	United States	anonymous	no	no	15 secs ago
# 195.114.209.50	80	ES	Spain	elite proxy	no	no	15 secs ago
# 142.44.210.174	80	CA	Canada	elite proxy	yes	no	15 secs ago
# 159.65.221.25	80	US	United States	anonymous	yes	no	15 secs ago
# 189.202.188.149	80	MX	Mexico	anonymous	no	no	15 secs ago
# 103.127.1.130	80	BD	Bangladesh	anonymous	no	no	15 secs ago
# 195.181.172.230	8082	NL	Netherlands	anonymous	no	no	15 secs ago
# 50.168.163.176	80	US	United States	anonymous	no	no	15 secs ago
# 50.174.145.11	80	US	United States	anonymous	no	no	15 secs ago
# 202.5.16.44	80	US	United States	anonymous	no	no	15 secs ago
# 133.18.234.13	80	JP	Japan	anonymous	no	no	15 secs ago
# 41.89.16.6	80	KE	Kenya	elite proxy	yes	no	15 secs ago
# 50.171.152.25	80	US	United States	anonymous	no	no	15 secs ago
# 50.200.12.81	80	US	United States	anonymous	no	no	15 secs ago
# 66.191.31.158	80	US	United States	anonymous	no	no	15 secs ago
# 50.174.216.104	80	US	United States	anonymous	no	no	15 secs ago
# 50.171.152.29	80	US	United States	anonymous	no	no	15 secs ago
# 50.170.90.29	80	US	United States	anonymous	no	no	15 secs ago
# 50.172.39.98	80	US	United States	anonymous	no	no	15 secs ago
# 50.172.218.164	80	US	United States	anonymous	no	no	15 secs ago
# 217.13.111.11	80	HU	Hungary	elite proxy	yes	no	15 secs ago
# 50.172.75.125	80	US	United States	anonymous	no	no	15 secs ago
# 96.113.158.126	80	US	United States	anonymous	no	no	15 secs ago
# 50.175.212.79	80	US	United States	anonymous	no	no	15 secs ago
# 46.101.115.59	80	DE	Germany	elite proxy	yes	no	15 secs ago
# 198.44.255.3	80	HK	Hong Kong	anonymous	no	no	15 secs ago
# 154.208.10.126	80	US	United States	anonymous	no	no	15 secs ago
# 50.200.12.85	80	US	United States	anonymous	no	no	15 secs ago
# 162.243.95.8	80	US	United States	elite proxy	no	no	15 secs ago
# 50.200.12.82	80	US	United States	anonymous	no	no	15 secs ago
# 43.250.107.223	80	HK	Hong Kong	anonymous	no	no	15 secs ago
# 79.137.199.255	8888	NL	Netherlands	anonymous	no	no	15 secs ago
# 50.217.29.198	80	US	United States	anonymous	no	no	15 secs ago
# 162.214.165.203	80	US	United States	elite proxy	yes	no	15 secs ago
# 50.168.89.184	80	US	United States	anonymous	no	no	15 secs ago
# 159.138.122.91	18081	SG	Singapore	anonymous	no	no	15 secs ago
# 190.58.248.86	80	TT	Trinidad and Tobago	anonymous	no	no	15 secs ago
# 50.174.7.154	80	US	United States	anonymous	no	no	15 secs ago
# 50.168.163.180	80	US	United States	anonymous	no	no	15 secs ago
# 50.204.190.234	80	US	United States	anonymous	no	no	15 secs ago
# 50.204.219.226	80	US	United States	anonymous	no	no	15 secs ago
# 82.119.96.254	80	SK	Slovakia	anonymous	no	no	15 secs ago
# 68.188.59.198	80	US	United States	anonymous	no	no	15 secs ago
# 50.218.57.65	80	US	United States	anonymous	no	no	15 secs ago
# 50.204.219.225	80	US	United States	anonymous	no	no	15 secs ago
# 139.59.1.14	8080	IN	India	anonymous	no	no	15 secs ago
# 138.201.51.183	9099	DE	Germany	elite proxy	no	yes	15 secs ago
# 50.204.219.228	80	US	United States	anonymous	no	no	15 secs ago
# 43.156.0.125	8888	SG	Singapore	anonymous	no	no	15 secs ago
# 50.173.140.148	80	US	United States	anonymous	no	no	15 secs ago
# 50.207.199.85	80	US	United States	anonymous	no	no	15 secs ago
# 216.137.184.253	80	US	United States	elite proxy	yes	no	15 secs ago
# 103.163.51.254	80	BD	Bangladesh	anonymous	no	no	15 secs ago
# 162.240.76.92	80	US	United States	elite proxy	yes	no	15 secs ago
# 123.30.154.171	7777	VN	Vietnam	anonymous	no	no	15 secs ago
# 198.176.56.44	80	US	United States	anonymous	yes	no	15 secs ago
# 80.150.50.226	80	DE	Germany	anonymous	no	no	15 secs ago
# 50.207.199.83	80	US	United States	anonymous	no	no	15 secs ago
# 172.232.97.161	80	IN	India	elite proxy	no	no	15 secs ago
# 41.230.216.70	80	TN	Tunisia	anonymous	no	no	15 secs ago
# 50.170.90.27	80	US	United States	anonymous	no	no	15 secs ago
# 50.168.163.181	80	US	United States	anonymous	no	no	15 secs ago
# 50.204.219.231	80	US	United States	anonymous	no	no	15 secs ago
# 96.113.159.162	80	US	United States	anonymous	no	no	15 secs ago
# 154.118.228.212	80	TZ	Tanzania	anonymous	no	no	15 secs ago
# 50.204.219.230	80	US	United States	anonymous	no	no	15 secs ago
# 50.218.57.64	80	US	United States	anonymous	no	no	15 secs ago
# 47.56.110.204	8989	HK	Hong Kong	anonymous	yes	no	15 secs ago
# 50.200.12.84	80	US	United States	anonymous	no	no	15 secs ago
# 50.168.72.112	80	US	United States	anonymous	no	no	15 secs ago
# 50.218.57.67	80	US	United States	anonymous	no	no	15 secs ago
# 198.176.56.43	80	US	United States	anonymous	yes	no	15 secs ago
# 72.55.172.166	5556	CA	Canada	elite proxy	yes	no	15 secs ago
# 69.48.179.103	80	US	United States	elite proxy	yes	no	15 secs ago
# 78.28.152.78	80	BA	Bosnia and Herzegovina	elite proxy	yes	no	15 secs ago
# 198.176.56.39	80	US	United States	anonymous	yes	no	15 secs ago
# 50.217.226.42	80	US	United States	anonymous	no	no	15 secs ago
# 20.111.54.16	8123	FR	France	elite proxy	no	no	19 secs ago
# 180.183.160.188	8080	TH	Thailand	transparent	no	no	1 min ago
# 103.122.60.241	8080	IN	India	transparent	no	no	2 mins ago
# 167.71.5.83	3128	NL	Netherlands	anonymous		no	10 mins ago
# 194.67.91.153	80	RU	Russian Federation	elite proxy	yes	no	10 mins ago
# 162.240.75.37	80	US	United States	elite proxy	yes	no	10 mins ago
# 167.99.124.118	80	US	United States	anonymous	yes	no	10 mins ago
# 162.223.94.164	80	US	United States	anonymous	no	no	10 mins ago
# 51.15.242.202	8888	FR	France	anonymous	no	no	10 mins ago
# 183.88.194.12	8080	TH	Thailand	transparent	no	no	10 mins ago
# 34.23.45.223	80	US	United States	elite proxy		no	10 mins ago
# 20.24.43.214	80	SG	Singapore	elite proxy	no	no	10 mins ago
# 20.206.106.192	80	BR	Brazil	elite proxy	no	no	10 mins ago
# 62.210.114.201	8080	FR	France	elite proxy		yes	10 mins ago
# 52.196.1.182	80	JP	Japan	elite proxy	no	yes	10 mins ago
# 191.96.251.53	80	BR	Brazil	elite proxy		no	10 mins ago
# 62.72.57.240	80	DE	Germany	elite proxy		no	10 mins ago
# 72.10.160.171	5369	CA	Canada	elite proxy		no	10 mins ago
# 114.156.77.107	8080	JP	Japan	elite proxy		no	10 mins ago
# 104.236.195.90	10009	US	United States	elite proxy		no	10 mins ago
# 75.89.101.63	80	US	United States	anonymous		no	10 mins ago
# 117.54.114.33	80	ID	Indonesia	anonymous		no	10 mins ago
# 209.97.150.167	3128	US	United States	anonymous	no	no	10 mins ago
# 182.253.112.187	80	ID	Indonesia	elite proxy		no	10 mins ago
# 188.166.56.246	80	NL	Netherlands	elite proxy	no	no	10 mins ago
# 132.226.14.0	80	JP	Japan	anonymous		no	10 mins ago
# 88.99.171.90	7003	DE	Germany	elite proxy		no	10 mins ago
# 195.201.42.194	6699	DE	Germany	elite proxy		no	10 mins ago
# 172.232.111.106	80	IN	India	elite proxy		no	10 mins ago
# 172.235.1.113	80	IN	India	elite proxy		no	10 mins ago
# 103.168.155.116	80	JP	Japan	anonymous	yes	no	10 mins ago
# 116.203.28.43	80	DE	Germany	anonymous	no	no	10 mins ago
# 207.2.120.15	80	US	United States	anonymous	yes	no	10 mins ago
# 103.137.62.253	80	TW	Taiwan	anonymous	no	no	10 mins ago
# 194.182.163.117	3128	CH	Switzerland	anonymous	no	no	10 mins ago
# 50.207.199.86	80	US	United States	anonymous	no	no	10 mins ago
# 49.228.131.169	5000	TH	Thailand	anonymous	no	no	10 mins ago
# 50.168.163.182	80	US	United States	anonymous	no	no	10 mins ago
# 50.174.145.9	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.72.119	80	US	United States	anonymous	no	no	10 mins ago
# 50.174.145.15	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.210.226	80	US	United States	anonymous	no	no	10 mins ago
# 50.171.152.26	80	US	United States	anonymous	no	no	10 mins ago
# 32.223.6.94	80	US	United States	anonymous	no	no	10 mins ago
# 77.48.244.78	80	CZ	Czech Republic	anonymous	no	no	10 mins ago
# 93.117.225.195	80	NL	Netherlands	anonymous	no	no	10 mins ago
# 50.168.210.239	80	US	United States	anonymous	no	no	10 mins ago
# 201.148.32.162	80	MX	Mexico	anonymous	no	no	10 mins ago
# 41.207.187.178	80	TG	Togo	anonymous	no	no	10 mins ago
# 50.222.245.40	80	US	United States	anonymous	no	no	10 mins ago
# 50.169.23.170	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.210.235	80	US	United States	anonymous	no	no	10 mins ago
# 50.200.12.86	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.210.234	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.210.236	80	US	United States	anonymous	no	no	10 mins ago
# 50.220.168.134	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.163.178	80	US	United States	anonymous	no	no	10 mins ago
# 50.218.57.71	80	US	United States	anonymous	no	no	10 mins ago
# 50.173.140.138	80	US	United States	anonymous	no	no	10 mins ago
# 50.217.226.47	80	US	United States	anonymous	no	no	10 mins ago
# 50.207.199.80	80	US	United States	anonymous	no	no	10 mins ago
# 213.33.126.130	80	AT	Austria	anonymous	no	no	10 mins ago
# 50.168.72.114	80	US	United States	anonymous	no	no	10 mins ago
# 50.207.199.81	80	US	United States	anonymous	no	no	10 mins ago
# 50.237.207.186	80	US	United States	anonymous	no	no	10 mins ago
# 50.168.72.113	80	US	United States	anonymous	no	no	10 mins ago
# 50.207.199.87	80	US	United States	anonymous	no	no	10 mins ago
# 85.26.146.169	80	RU	Russian Federation	anonymous	no	no	10 mins ago
# 50.217.226.41	80	US	United States	anonymous	no	no	10 mins ago
# 50.202.75.26	80	US	United States	anonymous	no	no	10 mins ago
# 127.0.0.7	80		Unknown	anonymous	no	no	10 mins ago
# 180.183.7.138	8080	TH	Thailand	transparent	no	no	12 mins ago
# 103.119.55.232	10001	ID	Indonesia	transparent	no	no	15 mins ago
# 200.106.124.14	999	PE	Peru	transparent	no	no	15 mins ago
# 188.40.44.83	80	DE	Germany	transparent	no	no	19 mins ago
# 78.28.152.113	80	BA	Bosnia and Herzegovina	elite proxy	yes	no	20 mins ago
# 80.13.43.193	80	FR	France	anonymous	yes	no	20 mins ago
# 209.126.6.159	80	US	United States	elite proxy	yes	no	20 mins ago
# 67.43.228.254	32221	CA	Canada	elite proxy	no	yes	20 mins ago
# 202.131.65.110	80	HK	Hong Kong	anonymous	yes	no	20 mins ago
# 162.243.184.21	10008	US	United States	elite proxy	yes	yes	20 mins ago
# 50.231.172.74	80	US	United States	anonymous	no	no	20 mins ago
# 162.223.116.75	80	CA	Canada	elite proxy	yes	no	20 mins ago
# 50.174.7.158	80	US	United States	anonymous	no	no	20 mins ago
# 50.173.140.147	80	US	United States	anonymous	no	no	20 mins ago
# 50.122.86.118	80	US	United States	anonymous	no	no	20 mins ago
# 50.222.245.42	80	US	United States	anonymous	no	no	20 mins ago
# 50.222.245.44	80	US	United States	anonymous	no	no	20 mins ago
# 213.143.113.82	80	AT	Austria	anonymous	no	no	20 mins ago
# 0.0.0.0	80		Unknown	anonymous	no	no	20 mins ago
# 50.172.75.124	80	US	United States	anonymous	no	no	20 mins ago
# 50.174.145.10	80	US	United States	anonymous	no	no	20 mins ago
# 50.175.212.74	80	US	United States	anonymous	no	no	20 mins ago
# 50.169.37.50	80	US	United States	anonymous	no	no	20 mins ago
# 50.239.72.19	80	US	United States	anonymous	no	no	20 mins ago
# 50.219.244.6	80	US	United States	anonymous	no	no	20 mins ago
# 50.172.75.121	80	US	United States	anonymous	no	no	20 mins ago
# 50.223.38.6	80	US	United States	anonymous	no	no	20 mins ago
# 50.174.214.222	80	US	United States	anonymous	no	no	20 mins ago
# 50.222.245.43	80	US	United States	anonymous	no	no	20 mins ago
# 50.222.245.41	80	US	United States	anonymous	no	no	20 mins ago
# 50.222.245.50	80	US	United States	anonymous	no	no	20 mins ago
# 50.172.75.126	80	US	United States	anonymous	no	no	20 mins ago
# 50.168.210.232	80	US	United States	anonymous	no	no	20 mins ago
# 143.198.226.25	80	US	United States	elite proxy	yes	no	20 mins ago
# 50.174.145.12	80	US	United States	anonymous	no	no	20 mins ago
# 50.174.7.162	80	US	United States	anonymous	no	no	20 mins ago
# 50.173.140.149	80	US	United States	anonymous	no	no	20 mins ago
# 50.168.163.179	80	US	United States	anonymous	no	no	20 mins ago
# 50.206.111.88	80	US	United States	anonymous	no	no	20 mins ago
# 50.174.7.152	80	US	United States	anonymous	no	no	20 mins ago
# 50.168.163.177	80	US	United States	anonymous	no	no	20 mins ago
# 50.235.240.86	80	US	United States	anonymous	no	no	20 mins ago
# 50.217.226.45	80	US	United States	anonymous	no	no	20 mins ago
# 50.174.7.157	80	US	United States	anonymous	no	no	20 mins ago
# 50.204.219.229	80	US	United States	anonymous	no	no	20 mins ago
# 50.239.72.18	80	US	United States	anonymous	no	no	20 mins ago
# 50.218.57.70	80	US	United States	anonymous	no	no	20 mins ago
# 50.217.226.43	80	US	United States	anonymous	no	no	20 mins ago
# 50.207.199.84	80	US	United States	anonymous	no	no	20 mins ago
# 50.173.140.145	80	US	United States	anonymous	no	no	20 mins ago
# 50.221.74.130	80	US	United States	anonymous	no	no	20 mins ago
# 50.168.163.183	80	US	United States	anonymous	no	no	20 mins ago
# 34.205.140.41	3128	US	United States	transparent	no	no	20 mins ago
# 50.170.90.25	80	US	United States	anonymous	no	no	20 mins ago
# 50.231.104.58	80	US	United States	anonymous	no	no	20 mins ago
# 162.222.207.221	80	US	United States	elite proxy	yes	no	20 mins ago
# 50.207.199.82	80	US	United States	anonymous	no	no	20 mins ago
# 50.217.226.40	80	US	United States	anonymous	no	no	20 mins ago
# 50.204.219.227	80	US	United States	anonymous	no	no	20 mins ago
# 50.239.72.16	80	US	United States	anonymous	no	no	20 mins ago
# 50.174.7.155	80	US	United States	anonymous	no	no	20 mins ago
# 50.204.219.224	80	US	United States	anonymous	no	no	20 mins ago
# 20.205.61.143	80	HK	Hong Kong	elite proxy	no	no	20 mins ago
# 35.72.118.126	80	JP	Japan	elite proxy	no	yes	20 mins ago
# 171.245.127.118	5000	VN	Vietnam	transparent	no	no	21 mins ago
# 154.202.110.245	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.98.159	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.122.137	3128	US	United States	transparent	no	no	21 mins ago
# 154.201.62.213	3128	US	United States	transparent	no	no	21 mins ago
# 154.201.62.237	3128	US	United States	transparent	no	no	21 mins ago
# 104.165.169.11	3128	US	United States	transparent	no	no	21 mins ago
# 154.84.143.11	3128	US	United States	transparent	no	no	21 mins ago
# 154.201.63.37	3128	US	United States	transparent	no	no	21 mins ago
# 154.84.143.195	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.97.2	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.109.244	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.120.49	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.108.233	3128	US	United States	transparent	no	no	21 mins ago
# 154.201.61.21	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.122.75	3128	US	United States	transparent	no	no	21 mins ago
# 154.201.63.183	3128	US	United States	transparent	no	no	21 mins ago
# 104.165.169.183	3128	US	United States	transparent	no	no	21 mins ago
# 154.202.96.41	3128	US	United States	transparent	no	no	21 mins ago
# 119.76.142.144	8080	TH	Thailand	transparent	no	no	22 mins ago
# 80.90.87.22	8083	AL	Albania	transparent	no	no	24 mins ago
# 202.153.233.228	8080	ID	Indonesia	transparent	no	no	24 mins ago
# 125.25.33.123	8080	TH	Thailand	transparent	no	no	24 mins ago
# 154.201.61.139	3128	US	United States	transparent	no	no	26 mins ago
# 154.201.61.157	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.120.31	3128	US	United States	transparent	no	no	26 mins ago
# 154.201.62.119	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.122.177	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.96.171	3128	US	United States	transparent	no	no	26 mins ago
# 104.252.131.95	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.109.254	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.99.24	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.97.84	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.108.135	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.120.99	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.96.235	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.96.79	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.111.26	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.96.7	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.121.106	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.109.144	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.97.58	3128	US	United States	transparent	no	no	26 mins ago
# 154.202.96.77	3128	US	United States	transparent	no	no	26 mins ago
# 20.27.86.185	80	JP	Japan	anonymous	no	yes	30 mins ago
# 119.207.95.158	8080	KR	South Korea	elite proxy	yes	yes	30 mins ago
# 77.77.64.120	3128	IR	Iran	anonymous		yes	30 mins ago
# 47.254.91.248	3773	US	United States	elite proxy	no	yes	30 mins ago
# 211.222.252.187	80	KR	South Korea	anonymous	no	no	30 mins ago
# 219.93.101.60	80	MY	Malaysia	anonymous	no	no	30 mins ago
# 138.68.60.8	8080	US	United States	anonymous	no	no	30 mins ago
# 117.250.3.58	8080	IN	India	elite proxy	no	yes	30 mins ago
# 188.166.17.18	8881	NL	Netherlands	anonymous	no	no	30 mins ago
# 18.228.198.164	80	BR	Brazil	elite proxy	no	yes	30 mins ago
# 188.165.213.106	80	FR	France	elite proxy	yes	no	30 mins ago
# 50.200.12.83	80	US	United States	anonymous	no	no	30 mins ago
# 50.171.152.28	80	US	United States	anonymous	no	no	30 mins ago
# 50.206.111.89	80	US	United States	anonymous	no	no	30 mins ago
# 50.200.12.80	80	US	United States	anonymous	no	no	30 mins ago
# 50.171.152.30	80	US	United States	anonymous	no	no	30 mins ago
# 68.185.57.66	80	US	United States	anonymous	no	no	30 mins ago"""
#
#     ip = []
#
#     rows = content.split("\n")
#     for r in rows:
#         tabs = r.split("\t")
#         ip.append(tabs[0].strip() + ":" + tabs[1].strip())
#
#     sf = ScraperFacade(None)
#     # sf.proxy_kit.proxy_list = ip
#     # response = sf.requests_scrape(url)
#     m = "firefox_selenium_scrape"
#     funct = getattr(sf, m)
#     print(funct(url))

    # *******************

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
