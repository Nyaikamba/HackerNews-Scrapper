import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
# print(res.text)

hacker_soup = BeautifulSoup(res.text, 'html.parser')


links = hacker_soup.select('.storylink')
subtext = hacker_soup.select('.subtext')


def custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        news_title = item.getText()
        news_link = item.get('href', None)
        news_votes = subtext[idx].select('.score')

        if len(news_votes):
            points = int(news_votes[0].getText().replace(' points', ' '))
            if (points>100):
                hacker_news.append({'title': news_title, 'link': news_link, 'points': points})

    return hacker_news


pprint.pprint(custom_hacker_news(links, subtext))
