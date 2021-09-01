from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)         #parent Window
time.sleep(2)

handles=driver.window_handles       #returns handle value of all the browsers
time.sleep(2)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()          #Close only parent window

time.sleep(2)
driver.quit()

