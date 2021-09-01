from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)

#driver.switch_to_alert().accept()  #closes alert window by clicking Ok

driver.switch_to_alert().dismiss()  #closes alert window by clicking Cancel

time.sleep(2)
driver.close()

