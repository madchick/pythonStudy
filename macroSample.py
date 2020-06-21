from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome('./chromedriver')
url = 'https://www.google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()
action.send_keys('madchick').perform()
driver.find_element_by_css_selector('.CwaK9').click()
time.sleep(2)

(
action
.key_down(Keys.TAB)
.key_down(Keys.TAB)
.send_keys('제목입니다').pause(2).key_down(Keys.TAB)
.send_keys('abcd').pause(2).key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('abcd').key_up(Keys.SHIFT)
.perform()
)