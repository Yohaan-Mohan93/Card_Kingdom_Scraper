from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from helper import create_directory

def get_set_name(set_url):
      name = set_url.split('/')[5]
      names = name.split('-')

      for i in range(len(names)):
            names[i] = names[i].capitalize()

      set_name = ' '.join(names).strip()
      return set_name

options = Options()
options.headless = True

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=options)
browser.get('https://starcitygames.com/shop/singles/#')

try:
      browser.find_element(By.CLASS_NAME, 'dropdown-trigger').click()
      dropdown = browser.find_element(By.CLASS_NAME,'set-select-container').find_element(By.CLASS_NAME,'tippy-box').\
            find_element(By.CLASS_NAME, 'tippy-content').find_element(By.CLASS_NAME, 'dropdown-list').\
            find_elements(By.TAG_NAME, 'li')[2].click()



      wait = WebDriverWait(browser,20)
      odd_year_list = wait.until(EC.presence_of_element_located((By.ID,'tab_list_1993')))
      current_year = int(date.today().strftime('%Y')) + 1
      url_dictionary = { }

      for year in range(1993,current_year):
            year_list = wait.until(EC.presence_of_element_located((By.ID,'tab_list_' + str(year))))
            set_list = year_list.find_element(By.CLASS_NAME,'content').find_elements(By.TAG_NAME,'li')
            for i in range(len(set_list) - 1 ,-1, -1):
                  set_url = set_list[i].find_element(By.TAG_NAME,'a').get_attribute('href')
                  set_name = get_set_name(set_url)
                  if 'Black Border' in set_name:
                        continue
                  url_dictionary[set_name] = set_url
                  print('Set Name: ', set_name, ', Set URL; ', set_url)

      path_to_file = 'Star_City_Games/URLs'
      result = create_directory(path_to_file)
      url_filename = path_to_file + '/scg_urls.txt'

      with open(url_filename,'w') as file_handle:
            file_handle.write('Set_Name|Set_URL')
            for key,value in url_dictionary.items():
                  file_handle.write('%s|%s\n' %(key,value))

except Exception as e:
      print("Failed because ", e)

