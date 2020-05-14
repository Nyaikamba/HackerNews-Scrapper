# libraries required

import requests
import pprint
from bs4 import BeautifulSoup


# Get data by looping through first 5 pages on HackerNews

def get_data():
    for i in range(1,5):
        res = requests.get('https://news.ycombinator.com/news?p={page}'.format(page =i))
        hacker_soup = BeautifulSoup(res.text, 'html.parser')
        links = hacker_soup.select('.storylink')
        subtext = hacker_soup.select('.subtext')

        return custom_hacker_news(links, subtext)


# Sort stories with highest ranked coming first

def sort_by_points(news_list):
    return sorted(news_list, key=lambda k: k['points'], reverse=True)


# Get data into a list, only add stories with more than 100 points

def custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        news_title = item.getText()
        news_link = item.get('href', None)
        news_votes = subtext[idx].select('.score')

        if len(news_votes):
            points = int(news_votes[0].getText().replace(' points', ' '))
            if (points > 99):
                hacker_news.append({'title': news_title, 'link': news_link, 'points': points})

    return sort_by_points(hacker_news)


pprint.pprint(get_data())
