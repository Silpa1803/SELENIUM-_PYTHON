from selenium import webdriver
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(2)

#1. scroll down page by Pixel:
#driver.execute_script("window.scrollBy(0,1500)","")

#2. scroll down the page till element found:
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#Scroll to end of the page:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(2)
driver.quit()

