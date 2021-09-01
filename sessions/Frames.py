from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame("packageListFrame")  #First Frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)

driver.switch_to.default_content()      #go back to default page

driver.switch_to.frame("packageFrame")      #second Frame
driver.find_element_by_link_text("JavascriptExecutor").click()
time.sleep(2)

driver.switch_to.default_content()      #go back to default page

driver.switch_to.frame("classFrame")    #third Frame
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[2]/a").click()
time.sleep(2)

driver.close()

