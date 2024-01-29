import bs4
import numpy as np
import pandas as pd


if __name__ == "__main__":


    path = "C:\\users\\dblin\\Downloads\\html_tmp\\a.html"
    with open(path, "r") as file:
        soup = bs4.BeautifulSoup(file, 'html.parser')
        table_html = soup.find('table', class_='tablesaw')
        # df =  pd.read_html(table_html)

    print(table_html)
    random_bits = np.random.randbits(10)

    print("Generated random bits:", random_bits)

    """
    TODO:
    - integration test
    - scrapy
    - sql alchemy db handler

    
    - clean up linter -> make into unittest, subtest for each dir, error if not 10
    - clean up regression + folders to exclude from linter
    - take PROJECT_FOLDER out of secrets.py -> setup.py
    
    ***TESTRUNNER
    unittest.TextTestRunner().run(suite)
    should be able to run tests and integrate with logger
    """


"""
REQUEST STRUCTURE


def dothedew(dodo):
    d = dodo.pop(0)
    print(d)
    # fail = 5 / 0


def runner(dl, func):

    while (len(dl) > 0):
        try:
            func(dl)
        except Exception:
            print("hoopsie")


if __name__ == "__main__":
    dolist = ["requests", "scrapy", "selenium", "pyppeteer"]

    runner(dolist, dothedew)
"""
