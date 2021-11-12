from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from helper import create_directory, sort_ck_urls
import csv

def get_ck_set_urls():
    scg_urls = []
    url = 'https://www.cardkingdom.com/catalog/magic_the_gathering/by_az'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' \
                 ' like Gecko) Chrome/94.0.4606.81 Safari/537.36'

    init = Request(url, headers={'User-Agent': user_agent})
    init_html = urlopen(init)
    init_bs = BeautifulSoup(init_html.read(), 'html.parser')
    urls = init_bs.select(".col-sm-6 a[href]")

    path_to_file = 'Card_Kingdom/URLs'
    result = create_directory(path_to_file)

    with open('./Card_Kingdom/URLs/ck_urls.txt', 'w') as f:
        f.write('Set_Name|Set_URL\n')
        for i in range(len(urls)):
            f.write('%s|%s\n' %(urls[i].getText(),urls[i]['href']))
        f.close()
