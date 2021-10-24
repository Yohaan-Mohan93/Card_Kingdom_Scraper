from ck_scraper import *
import os


def find_number_of_pages(cknf):
    cknf_start_url = 'https://www.cardkingdom.com/catalog/view?filter%5Bipp%5D=20&filter%5Bsort%5D=name&filter' \
                     '%5Bsearch%5D=mtg_advanced&filter%5Bcategory_id%5D=0&filter%5Bmulti%5D%5B0%5D=1&filter' \
                     '%5Btype_mode%5D=any&filter%5Bmanaprod_select%5D=any'

    ckf_start_url = 'https://www.cardkingdom.com/catalog/view?filter%5Bipp%5D=20&filter%5Bsort%5D=name&filter%5Bsearch' \
                    '%5D=mtg_advanced&filter%5Btab%5D=mtg_foil&filter%5Bcategory_id%5D=0&filter%5Bmulti%5D%5B0%5D=1' \
                    '&filter%5Btype_mode%5D=any&filter%5Bmanaprod_select%5D=any'

    result = 0

    if cknf:
        result = scrape_page_numbers(cknf_start_url)
    else:
        result = scrape_page_numbers(ckf_start_url)

    return result


def create_directory(path_to_file):
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)

    return os.path.exists(path_to_file)
