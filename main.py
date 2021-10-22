from ck_scraper import scrape, scrape_page_numbers
from datetime import date
import os

cknf_start_url = 'https://www.cardkingdom.com/catalog/view?filter%5Bipp%5D=20&filter%5Bsort%5D=name&filter' \
                 '%5Bsearch%5D=mtg_advanced&filter%5Bcategory_id%5D=0&filter%5Bmulti%5D%5B0%5D=1&filter' \
                 '%5Btype_mode%5D=any&filter%5Bmanaprod_select%5D=any'

ckf_start_url = 'https://www.cardkingdom.com/catalog/view?filter%5Bipp%5D=20&filter%5Bsort%5D=name&filter%5Bsearch' \
                '%5D=mtg_advanced&filter%5Btab%5D=mtg_foil&filter%5Bcategory_id%5D=0&filter%5Bmulti%5D%5B0%5D=1' \
                '&filter%5Btype_mode%5D=any&filter%5Bmanaprod_select%5D=any'


if not os.path.exists('Card_Kingdom'):
    os.makedirs('Card_Kingdom')

date_today = date.today().strftime('%dd%mm%yyyy')

cknf_cards_filename = 'Card_Kingdom/CK_CARDS_' + date_today +'.txt'
cknf_urls_filename = 'Card_Kingdom/CK_CARDS_' + date_today +'.txt'

with open(cknf_cards_filename, 'w') as file_handle:
    file_handle.write("Name|Type|Set|Rarity|NM(USD)|EX(USD)|VG(USD)|G(USD)\n")

print("Starting Scraping")
last_page_number = scrape_page_numbers(cknf_start_url)
print("The last page is ", last_page_number)
scrape(cknf_start_url, cknf_cards_filename, cknf_urls_filename)