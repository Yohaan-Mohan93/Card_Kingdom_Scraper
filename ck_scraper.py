from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from ck_mtg_card import *
import re


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' \
                 ' like Gecko) Chrome/94.0.4606.81 Safari/537.36'


def has_number(input_string):
    return bool(re.search(r'\d', input_string))


def scrape_page_numbers(url):
    url = url
    global user_agent
    this_user_agent = user_agent
    init = Request(url, headers={'User-Agent': this_user_agent})
    init_html = urlopen(init)
    init_bs = BeautifulSoup(init_html.read(), 'html.parser')
    final_page = int(init_bs.find_all(class_='btn btn-default col-xs-4')[1].getText().split(' ')[3])

    return final_page


def scrape(start_url, card_list, urls, all_cards_placements, page_number):
    try:
        url = start_url
        global user_agent
        this_user_agent = user_agent
        set_count = 0
        price_count = 0

        init = Request(url, headers={'User-Agent': this_user_agent})
        html = urlopen(init)
        bs = BeautifulSoup(html.read(), 'html.parser')
        urls.append(url)
        card_names = bs.find_all(class_='productDetailTitle')
        card_types = bs.find_all(class_='productDetailType')
        card_sets = bs.find_all(class_='productDetailSet')
        card_prices = bs.find_all(class_='stylePrice')
        card_id = int(bs.find_all(class_='resultsHeader')[0].getText().split(' ')[0])
        card_texts = bs.find_all(class_='detailFlavortext')

        for names in card_names:
            this_name = names.getText().strip()
            card_type = card_types[set_count].getText()[1:len(card_types[set_count].getText())]
            this_type = ''
            if has_number(card_type):
                types = re.split('(\d+)', card_type)
                this_type = types[len(types) - 1]
            else:
                this_type = card_type
            this_set_rarity = card_sets[set_count].getText().strip().split('(')
            this_nm = 0.0
            this_ex = 0.0
            this_vg = 0.0
            this_g = 0.0
            this_text = card_texts[set_count].getText().strip()
            set_count += 1

            for j in range(4):
                string = card_prices[price_count].getText().strip()
                if j == 0:
                    this_nm = float(string[1:len(string)])
                elif j == 1:
                    this_ex = float(string[1:len(string)])
                elif j == 2:
                    this_vg = float(string[1:len(string)])
                elif j == 3:
                    this_g = float(string[1:len(string)])
                price_count += 1

            this_set = this_set_rarity[0]
            this_rarity = this_set_rarity[1][0]

            card_list.append(CkMtgCard(card_id, this_name, this_type, this_set,
                                       this_rarity, this_nm, this_ex, this_vg, this_g,this_text))
            all_cards_placements.append(CkCardPlacement(this_name, this_set, set_count, page_number))
            card_id += 1

    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
        print(url, ' is wrong')

