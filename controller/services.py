import multiprocessing
import time
from functools import partial
from urllib import request

import requests

from webscraper.request_service import RequestManager

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

    rq = RequestManager("proxies_test.csv")
    response = rq.request_response(url)
    # response = rq.request_response_proxy(url)

    print(response.text)


# if proxy=False then None, else grab proxy from csvtolist
# cp = ContentProvider(None)
# funct = getattr(cp, scrape_method)

# response = funct(url)
# print("176.63.13.165" in response.text)



