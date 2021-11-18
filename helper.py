import os
import csv
import re

def has_number(input_string):
    return bool(re.search(r'\d', input_string))

def create_directory(path_to_file):
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)

    return os.path.exists(path_to_file)

def load_urls(website):
    urls = []
    if website == 'CardKingdom':
        with open('./Card_Kingdom/URLs/ck_urls.txt', 'r') as f:
            url_reader = csv.reader(f, delimiter='|')
            next(url_reader)
            urls = list(url_reader)
    elif website == 'SCG':
        with open('./Star_City_Games/URLs/scg_urls.txt', 'r') as f:
            url_reader = csv.reader(f, delimiter='|')
            next(url_reader)
            urls = list(url_reader)

    return urls