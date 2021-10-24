from ck_scraper import scrape
from datetime import date
from helper import *
import time
import threading


def scraping_task(the_card_list, the_urls, card_placements, start_page, end_page):
    for i in range(start_page, end_page, 1):
        url = "https://www.cardkingdom.com/catalog/view?filter%5Bipp%5D=20&filter%5Bsort%5D=name&filter%5Bsearch%" \
              "5D=mtg_advanced&filter%5Bcategory_id%5D=0&filter%5Bmulti%5D%5B0%5D=1&filter%5Btype_mode%5D=any&filter" \
              "%5Bmanaprod_select%5D=any&page=" + str(i)
        print("Page: ", i)
        scrape(url, the_card_list, the_urls, card_placements, i)
        print("Number of Cards: ", len(card_list))
        print("Number of Card Placements: ", len(all_card_placements))


if __name__ == "__main__":
    urls = []
    card_list = []
    all_card_placements = []
    date_today = date.today().strftime('%d%m%Y')
    path_to_file = 'Card_Kingdom/' + date_today
    start_time = time.time()
    scrape_size = 1

    result = create_directory(path_to_file)

    if result:
        print("Directory created")
    else:
        print("Directory exists")

    cknf_prices_filename = path_to_file + '/CK_PRICES_' + date_today + '.txt'
    cknf_cards_filename = path_to_file + '/CK_CARDS_' + date_today + '.txt'
    cknf_urls_filename = path_to_file + '/CK_URLS_' + date_today + '.txt'

    print("Starting Scraping")

    last_page_number = find_number_of_pages(True)
    scrape_increment = int(last_page_number/4)
    print("The last page is ", last_page_number)

    scrape_size += scrape_increment
    thread1 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, 1, scrape_size))

    temp = scrape_size
    scrape_size += scrape_increment
    thread2 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, temp, scrape_size))

    temp = scrape_size
    scrape_size += scrape_increment
    thread3 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, temp, scrape_size))

    temp = scrape_size
    thread4 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, temp, last_page_number))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("Scraping ended")

    card_list.sort(key=lambda card: card.name)
    all_card_placements.sort(key=lambda card: card.name)

    with open(cknf_prices_filename, 'w') as file_handle:
        file_handle.write("Name|Type|Set|Rarity|NM(USD)|EX(USD)|VG(USD)|G(USD)\n")
        for list_item in card_list:
            file_handle.write('%s\n' % list_item.to_string())

    with open(cknf_cards_filename, 'w') as file_handle:
        file_handle.write("Name|Set|Place In Page |Page Number\n")
        for list_item in all_card_placements:
            file_handle.write('%s\n' % list_item.to_string())

    end_time = time.time()
    time_taken_hrs = (end_time - start_time) / 60

    with open(cknf_urls_filename, 'w') as file_handle:
        for list_item in urls:
            file_handle.write('%s\n' % list_item)
        time_string = 'Total Execution Time: ' + str(time_taken_hrs) + ' minutes'
        file_handle.write('%s' % time_string)