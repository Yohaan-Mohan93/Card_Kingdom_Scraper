from datetime import date
from helper import *
from CK_Py_Scripts.ck_scraper import scrape
from CK_Py_Scripts.ck_mtg_card import *
import shutil
import time
import threading


def ck_scraping_task(start_url, set_name, the_card_list, the_urls, card_placements):
    edition = start_url[5:]
    print(edition)
    url = 'https://www.cardkingdom.com/catalog/search?search=mtg_advanced&filter%5Bsort%5D=name&filter%' \
          '5Bsearch%5D=mtg_advanced&filter%5Btab%5D=mtg_card&filter%5Bname%5D=&filter%5Bedition%5D=' + edition +'&' \
          'filter%5Btype_mode%5D=any&filter%5Bcard_type%5D%5B10%5D=&filter%5Bpow1%5D=&filter%5Bpow2%5D=&filter%5Btuf1' \
          '%5D=&filter%5Btuf2%5D=&filter%5Bconcast1%5D=&filter%5Bconcast2%5D=&filter%5Bprice_op%5D=&filter%5Bprice%5D=' \
          '&filter%5Boracle_text%5D=&filter%5Bmanaprod_select%5D=any'
    print("Set: ", set_name )
    print("Url: ", url)
    scrape(url, the_card_list, the_urls, card_placements)
    print("Number of Cards: ", len(card_list))
    print("Number of Card Placements: ", len(all_card_placements))


if __name__ == "__main__":
    visited_urls = []
    card_list = []
    all_card_placements = []
    date_today = date.today().strftime('%d%m%Y')
    path_to_file = 'Card_Kingdom/' + date_today
    start_time = time.time()
    urls = load_urls("CardKingdom")
    result = create_directory(path_to_file)

    if result:
        print("Directory created")
    else:
        print("Directory exists")

    cknf_prices_filename = path_to_file + '/CK_PRICES_' + date_today + '.txt'
    cknf_cards_filename = path_to_file + '/CK_CARDS_' + date_today + '.txt'
    cknf_urls_filename = path_to_file + '/CK_URLS_' + date_today + '.txt'

    print("Starting Scraping")

    ck_scraping_task(urls[0][1],urls[0][0],card_list,visited_urls,all_card_placements)

    #scrape_increment = int(last_page_number/4)
    #print("The last page is ", last_page_number)
    #
    #scrape_size += scrape_increment
    #thread1 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, 1, scrape_size))
    #
    #temp = scrape_size
    #scrape_size += scrape_increment
    #thread2 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, temp, scrape_size))
    #
    #temp = scrape_size
    #scrape_size += scrape_increment
    #thread3 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, temp, scrape_size))
    #
    #temp = scrape_size
    #thread4 = threading.Thread(target=scraping_task, args=(card_list, urls, all_card_placements, temp, (last_page_number + 1)))
    #
    #thread1.start()
    #thread2.start()
    #thread3.start()
    #thread4.start()
    #
    #thread1.join()
    #thread2.join()
    #thread3.join()
    #thread4.join()
    #
    #print("Scraping ended")
    #
    card_list = sorted(card_list ,key=lambda x : x.id)
    all_card_placements.sort(key=lambda card: card.name)
    
    with open(cknf_prices_filename, 'w') as file_handle:
        file_handle.write("ID|Name|Type|Set|Rarity|NM(USD)|EX(USD)|VG(USD)|G(USD)|Card Text\n")
        for list_item in card_list:
            file_handle.write('%s\n' % list_item.to_string())
    
    with open(cknf_cards_filename, 'w') as file_handle:
        file_handle.write("Name|Set|Place In Page |Page Number\n")
        for list_item in all_card_placements:
            file_handle.write('%s\n' % list_item.to_string())
    
    end_time = time.time()
    time_taken_hrs = (end_time - start_time) / 60
    
    with open(cknf_urls_filename, 'w') as file_handle:
        for list_item in visited_urls:
            file_handle.write('%s\n' % list_item)
        time_string = 'Total Execution Time: ' + str(time_taken_hrs) + ' minutes'
        file_handle.write('%s' % time_string)
    
    #shutil.make_archive(base_name=date_today,format='zip',root_dir='Card_Kingdom/' + date_today)
    #
    #target = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/CK_PRICES_' + date_today + '.txt';
    #shutil.copyfile(cknf_prices_filename, target)
    #shutil.copyfile(date_today + ".zip", 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/' + date_today + '.zip')
    #os.remove(date_today + '.zip')
    #
    #results = create_directory('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/' + date_today)
    #shutil.unpack_archive(filename='C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/' + date_today + '.zip',
    #                      format='zip',extract_dir='C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/' + date_today)