from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
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
            for i in range(len(set_list),0):
                  set_name = set_list[i].text
                  set_url = set_list[i].find_element(By.TAG_NAME,'a').get_attribute('href')
                  url_dictionary[set_name] = set_url
                  print('Set Name: ', set_name, ', Set URL; ', set_url)

      with open('scg_urls.txt','w') as file_handle:
            file_handle.write('Set_Name|Set_URL')
            for key,value in url_dictionary.items():
                  file_handle.write('%s|%s\n' %(key,value))

except Exception as e:
      print("Failed because ", e)
#li = odd_year_list.find_element(By.CLASS_NAME,'content').find_elements(By.TAG_NAME, 'li')
#print('Section ', odd_year_list.find_element_by_tag_name('h3').text ,' : ' ,
 #     len(li), li[0].find_element_by_tag_name('a').get_attribute('href'), li[0].text)

