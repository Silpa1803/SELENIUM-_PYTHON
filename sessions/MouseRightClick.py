from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)

element=driver.find_element_by_xpath("//*[@id='authentication']/span")

actions=ActionChains(driver)
actions.context_click(element).perform() #perform double click on the element
time.sleep(3)

driver.find_element_by_xpath("//*[@id='authentication']/ul/li[1]").click()

time.sleep(4)
driver.quit()

