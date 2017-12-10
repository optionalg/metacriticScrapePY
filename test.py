import requests
import string
import simplejson as json
import datetime
from bs4 import BeautifulSoup as bs

url = 'https://www.metacritic.com/browse/movies/title/dvd'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = bs(page.text, 'lxml')


def findDetails():
    details = soup.find_all('div', attrs={'class':'details_section'})
    for detail in details:
        print(detail.div)


findDetails()
