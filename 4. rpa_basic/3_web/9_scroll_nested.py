import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')

time.sleep(5)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[63]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view # 함수가 이닌까 () 쓰지 마세요
print("type : ", type(xy))
print("value : ", xy)

time.sleep(5)
browser.quit()

