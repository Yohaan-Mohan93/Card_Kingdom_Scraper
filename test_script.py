from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

edition = '3rd-edition'
print(edition)
url = 'https://www.cardkingdom.com/catalog/search?search=mtg_advanced&filter%5Bsort%5D=name&filter%' \
      '5Bsearch%5D=mtg_advanced&filter%5Btab%5D=mtg_card&filter%5Bname%5D=&filter%5Bedition%5D=' + edition + '&' \
      'filter%5Btype_mode%5D=any&filter%5Bcard_type%5D%5B10%5D=&filter%5Bpow1%5D=&filter%5Bpow2%5D=&filter%5Btuf1' \
      '%5D=&filter%5Btuf2%5D=&filter%5Bconcast1%5D=&filter%5Bconcast2%5D=&filter%5Bprice_op%5D=&filter%5Bprice%5D=' \
      '&filter%5Boracle_text%5D=&filter%5Bmanaprod_select%5D=any'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' \
             ' like Gecko) Chrome/94.0.4606.81 Safari/537.36'

options = Options()
options.headless = True

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
                           #options=options)
browser.get(url)
links = browser.find_elements(By.CSS_SELECTOR, '.page-item a')
card_names = browser.find_elements(By.CLASS_NAME, 'productDetailTitle')
card_types =browser.find_elements(By.CLASS_NAME,'productDetailType')
card_sets =browser.find_elements(By.CLASS_NAME,'productDetailSet')
card_prices =browser.find_elements(By.CLASS_NAME,'stylePrice')
card_texts =browser.find_elements(By.CLASS_NAME,'detailFlavortext')

print('Length: ', len(links))
print('Length: ', len(card_names))

for card_name in card_names:
    print(card_name.text)

print('Length: ', len(card_types))
print('Length: ', len(card_sets))
print('Length: ', len(card_prices))
print('Length: ', len(card_texts))
links[4].click()