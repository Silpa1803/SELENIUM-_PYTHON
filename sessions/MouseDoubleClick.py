from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)
actions.double_click(element).perform() #perform double click on the element

time.sleep(2)
driver.quit()

