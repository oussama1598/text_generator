import requests
from bs4 import BeautifulSoup


def get_content(article_link):
    response = requests.get(
        article_link,
    )
    response.encoding = 'utf-8'

    return BeautifulSoup(response.text, 'html5lib').find(id='content').text
