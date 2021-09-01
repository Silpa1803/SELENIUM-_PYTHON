from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#multibrowser open
driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://www.google.com/")

driver.maximize_window()

driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_name("btnK").click()

print(driver.title)   #title of the page

print(driver.current_url)   #returns URL of the page

print(driver.page_source)   #retruns code for the page

#driver.close()      #close currently focused browser
#driver.quit()      #close all the browsers


