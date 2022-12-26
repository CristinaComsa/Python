import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
my_browser = webdriver.Chrome(service=service)
"""
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
"""

# my_browser.get('https://formy-project.herokuapp.com/')
# my_browser.maximize_window()
# butons = my_browser.find_elements(By.XPATH, '//a[@class="btn btn-lg"]')
# butons[1].click()
# time.sleep(2)
# butons = my_browser.find_element(By.XPATH, '//button[text()="Primary"]')
# butons.click()
# time.sleep(2)
# butons = my_browser.find_element(By.XPATH, '//button[text()="Success"]')
# butons.click()
# time.sleep(2)
#
# my_browser.get('https://formy-project.herokuapp.com/')
# my_browser.maximize_window()
# list_butons = my_browser.find_elements(By.XPATH,'//a[@class="btn btn-lg"]' )
# list_butons[8].click()
# time.sleep(2)
#
#
# my_browser.get('https://formy-project.herokuapp.com/keypress')
# my_browser.maximize_window()
# keyboard = my_browser.find_element(By.CSS_SELECTOR, '#name')
# keyboard.send_keys('Comsa Cristina')
# time.sleep(2)
#
# my_browser.get('https://formy-project.herokuapp.com/scroll')
# my_browser.maximize_window()
# full_name = my_browser.find_element(By.CLASS_NAME, 'form-control')
# full_name.send_keys('Comsa Cristina')
# date = my_browser.find_element(By.CSS_SELECTOR, '#date')
# date.send_keys('11/03/2022')
# time.sleep(2)
#
# my_browser.get('https://formy-project.herokuapp.com/radiobutton')
# my_browser.maximize_window()
# radio_butons = my_browser.find_elements(By.CLASS_NAME, 'form-check-input')
#
# for i in range(0,3):
#     radio_butons[i].click()
# time.sleep(2)

# my_browser.get('https://www.techlistic.com/p/selenium-practice-form.html')
# my_browser.maximize_window()
# automation_practice = my_browser.find_element(By.ID,'ez-accept-all').click()
# time.sleep(3)
# first_name = my_browser.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
# first_name.send_keys('Cristina')
# time.sleep(2)
# last_name = my_browser.find_element(By.XPATH,'//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')
# last_name.send_keys('Comsa')
# time.sleep(2)
# gender = my_browser.find_element(By.ID,'sex-1').click()
# time.sleep(2)
# experience = my_browser.find_elements(By.XPATH,'//*[@type="radio"]')
# for i in range(0,9):
#     if i == 2: #din lista de la 0-9 elemente, experienta 1 an aferent index 2
#         experience[i].click()
# time.sleep(2)
# date = my_browser.find_element(By.ID,'datepicker').send_keys('07/11/2022')
# time.sleep(2)
# profession = my_browser.find_elements(By.XPATH, '//*[@type="checkbox"]')
# for i in range(len(profession)):
#     if i == 1:
#         profession[i].click()
# time.sleep(2)
# continents = my_browser.find_element(By.ID,'continents')
# continents.send_keys('Europe')
# time.sleep(2)

# my_browser.get('https://the-internet.herokuapp.com/')
# add_remove = my_browser.find_element(By.XPATH,'//*[@id="content"]/ul/li[2]/a')
# add_remove.click()
# time.sleep(2)
# add_element = my_browser.find_element(By.XPATH,'//*[@id="content"]/div/button')
# add_element.click()
# time.sleep(2)
# delete_element = my_browser.find_element(By.CSS_SELECTOR,'#elements > button')
# delete_element.click()
# time.sleep(2)

# my_browser.get('https://the-internet.herokuapp.com/checkboxes')
# check_box = my_browser.find_element(By.XPATH,'//*[@type="checkbox"]')
# check_box.click()
# time.sleep(2)

my_browser.get('https://the-internet.herokuapp.com/inputs')
number = my_browser.find_element(By.XPATH,'//*[@id="content"]/div/div/div/input')
number.send_keys(3)
time.sleep(2)
