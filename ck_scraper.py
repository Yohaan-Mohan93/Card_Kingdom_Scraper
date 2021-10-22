from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import time
import re

number = 2


def has_number(input_string):
    return bool(re.search(r'\d', input_string))


def scrape_page_numbers(url):
    url = url
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' \
                 ' like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    init = Request(url, headers={'User-Agent': user_agent})
    init_html = urlopen(init)
    init_bs = BeautifulSoup(init_html.read(), 'html.parser')
    final_page = int(init_bs.find_all(class_='btn btn-default col-xs-4')[1].getText().split(' ')[3])

    return final_page


def scrape(start_url, filename, url_filename):
    try:
        start_time = time.time()
        url = start_url
        global number
        page_number = number
        card_list = []
        urls = []

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' \
                     ' like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        init = Request(url, headers={'User-Agent': user_agent})
        init_html = urlopen(init)
        init_bs = BeautifulSoup(init_html.read(), 'html.parser')
        final_page = int(init_bs.find_all(class_='btn btn-default col-xs-4')[1].getText().split(' ')[3])
        print('last page is ', final_page)

    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
        print(url, ' is wrong')

