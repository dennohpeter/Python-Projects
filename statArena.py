from bs4 import BeautifulSoup
import requests
import re
from itertools import chain

page = requests.get("https://www.statarea.com/predictions", timeout=10)
try:
    page.raise_for_status()
except Exception as error:
    print('There was a problem getting cash1 data: %s' % error)
arena = BeautifulSoup(page.text, 'html.parser')
games_store = []
if type(arena) == BeautifulSoup:
    games = arena.findAll(class_="cmatch")
    games_num = len(games)
    get_algo = re.compile(
        r'''(
        \d+:\d+)\s+   
        (12|1X|1|2|X2|X)*
        (\s*\d+\s*:\d+\s*)*
        (.*)
        ''', re.VERBOSE)
    for each in games:
        print(each.getText())
        b = list(chain(*get_algo.findall(each.getText())))
        b[0:0] = ["shit"]  # inserting date
        games_store.append(b)

    print(games_store)
else:
    print("not bs4 obj")

