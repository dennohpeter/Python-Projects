from bs4 import BeautifulSoup
import requests
import re

page = requests.get("http://www.soccervista.com/bet.php",timeout=10)
try:
    page.raise_for_status()
except Exception as error:
    print('There was a problem getting cash1 data: %s' % error)
vista = BeautifulSoup(page.text, 'html.parser')
if type(vista) == BeautifulSoup:
    if "blocked" in page.text:
        print ("we've been blocked")
##    tr:nth-child(even)
    games = vista.select("tr:nth-child(even)")
    games_num = len(games)
    for each in games:
        print(each.getText()+"\n")
else:
    print("not bs4 obj")
