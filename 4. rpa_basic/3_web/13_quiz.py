from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
#browser.maximize_window()

browser.get('https://www.w3schools.com')

browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()

browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]').click()


first_name = '나도'
last_name = '코딩'
country = 'Canada'
subject = '퀴즈 완료하였습니다.'


browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
browser.find_element(By.XPATH, '//*[@id="country"]/option[text()={}]'.format(country)).click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)

browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()