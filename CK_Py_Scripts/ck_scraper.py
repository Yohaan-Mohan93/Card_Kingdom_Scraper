from urllib.error import HTTPError, URLError
from .ck_mtg_card import *
from helper import *
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape(start_url, card_list, urls, all_cards_placements):
    try:
        url = start_url
        options = Options()
        options.headless = True
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        browser.get(url)
        wait = WebDriverWait(browser, 20)

        pages =  wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.page-item a')))
        total_pages = pages[len(pages) - 2 ].text
        page_number = 1

        while(page_number <= (total_pages)):
            urls.append(url)
            set_count = 0
            price_count = 0
            card_names = browser.find_elements(By.CLASS_NAME, 'productDetailTitle')
            card_types = browser.find_elements(By.CLASS_NAME, 'productDetailType')
            card_sets = browser.find_elements(By.CLASS_NAME, 'productDetailSet')
            card_prices = browser.find_elements(By.CSS_SELECTOR,'input[name~="price"')
            card_texts = browser.find_elements(By.CLASS_NAME, 'detailFlavortext')

            for names in card_names:
                this_name = names.text.strip()
                card_type = card_types[set_count].text[1:len(card_types[set_count].text)]
                this_type = ''
                if has_number(card_type):
                    types = re.split('(\d+)', card_type)
                    this_type = types[len(types) - 1].strip()
                else:
                    this_type = card_type.strip()
                this_set_rarity = card_sets[set_count].text.strip().split('(')
                this_nm = 0.0
                this_ex = 0.0
                this_vg = 0.0
                this_g = 0.0
                this_text = card_texts[set_count].text.strip().replace('\n', ' ')
                set_count += 1

                for j in range(4):
                    string = card_prices[price_count].get_attribute("value").strip()
                    if j == 0:
                        this_nm = float(string)
                    elif j == 1:
                        this_ex = float(string)
                    elif j == 2:
                        this_vg = float(string)
                    elif j == 3:
                        this_g = float(string)
                    price_count += 1

                this_set = this_set_rarity[0]
                this_rarity = this_set_rarity[1][0]

                card_list.append(CkMtgCard(0, this_name, this_type, this_set,
                                           this_rarity, this_nm, this_ex, this_vg, this_g,this_text))
                all_cards_placements.append(CkCardPlacement(this_name, this_set, set_count, page_number))


            pages = browser.find_elements(By.CSS_SELECTOR,'.page-item a')
            page_number += 1
            print("Number of Cards: ", len(card_list))
            print("Number of Card Placements: ", len(all_cards_placements))
            if page_number != total_pages:
                print("Page Number: ", page_number)
                pages[len(pages) - 1].click()

    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
        print(url, ' is wrong')

