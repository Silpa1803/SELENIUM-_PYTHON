from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://www.expedia.co.in/")
time.sleep(5)   #from Python

driver.maximize_window()
print(driver.title)

driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a").click()  #click on flight
time.sleep(2)

driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/div/li[2]/a").click() #click on one-way
time.sleep(2)

leavingfrom=driver.find_element_by_css_selector("button[class=uitk-faux-input]")
leavingfrom.click()
time.sleep(3)
leavingfrom.send_keys(" Bhubaneshwar (BBI - Biju Patnaik)")
time.sleep(3)
driver.find_element_by_css_selector("button[data-stid='location-field-leg1-origin-result-item-button']").click()
print("leaving From Entered")
time.sleep(2)

goingto=driver.find_element_by_css_selector("button[aria-label='Going to']")
goingto.click()
time.sleep(3)
goingto.send_keys(" Bengaluru (BLR - Kempegowda Intl.)")
time.sleep(3)
driver.find_element_by_css_selector("button[data-stid='location-field-leg1-destination-result-item-button']").click()
print("Going To Entered")

traveldate=driver.find_element_by_css_selector("button[aria-label='Departing 9 September 2021']")
traveldate.click()
time.sleep(3)
driver.find_element_by_css_selector("button[aria-label='17 Sep 2021']").click()
driver.find_element_by_css_selector("button[data-stid='apply-date-picker']").click()

print("Date Entered")

driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click() #search

#ExplicitWait
wait=WebDriverWait(driver,15)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stops-0']")))
element.click()

#or you write in below way
#driver.find_element_by_xpath("//*[@id='stops-0']").click()
#print("0 Stops Selected")

time.sleep(3)
driver.close()