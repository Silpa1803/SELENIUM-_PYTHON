from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://www.expedia.co.in/")
driver.maximize_window()

time.sleep(3)
links=driver.find_elements(By.CLASS_NAME,"uitk-link uitk-link-layout-inline uitk-type-200")
print("Total number of Links present is: ",len(links))   #number of links present

for link in links:
    print(link.text)        #Print all the link names

#clicking the link

driver.find_element_by_link_text("Support").click()
#or
#driver.find_element_by_partial_link_text("Supp").click()

time.sleep(2)
driver.close()

