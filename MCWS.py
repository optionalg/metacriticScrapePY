import requests
import string
import simplejson as json
import datetime
from bs4 import BeautifulSoup as bs

date = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
f = open('./scrapedData/' + 'moviesDVD' + date + '.json', 'w')

titlesList = []
scoreList = []
mainList = []
linkList = []

i = 0

# array of the entire alphabet
# alphabet = list(string.ascii_lowercase)
alphabet = ['a']
# base url to be scraped
url = 'https://www.metacritic.com/browse/movies/title/dvd'

def printMessage(message, url):
    print(message + url)

def findTitles(): # scrape titles
    titles = soup.select('td.title_wrapper div.title a')
    for title in titles:
        linkList.append('https://www.metacritic.com' + title.get('href'))
        titlesList.append(title.text)


def findScores(): # scrape scores
    scores = soup.select('a.metascore_anchor div.metascore_w.large.movie')
    for score in scores:
        scoreList.append(score.text)
    return scoreList

def findDetails():
    userScores = soup.select('tr.details_row div.details_section div.userscore_text span')[1::2]
    for userScore in userScores:
        userScoreList.append(userScore.text.strip())

    return userScoreList



while url:
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = bs(page.text, 'lxml')
    url = soup.select('span.flipper.next a.action')

    findScores()
    findTitles()


    if url:
        url = 'https://www.metacritic.com' + url[0].get('href')
        print('Scraping: ' + url)
    else:
        if i < len(alphabet):
            url = 'http://www.metacritic.com/browse/movies/title/dvd/' + alphabet[i]
            i += 1
        else:
            print('Finished scraping. Have a nice day')
            break

mainList = [{'title': title, 'score': score, 'link': link} for title, score, link in zip(titlesList, scoreList, linkList)]

f.write(json.dumps(mainList))
f.close()

print(mainList)
