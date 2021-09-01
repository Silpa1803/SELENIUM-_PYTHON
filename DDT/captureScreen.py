import time

from selenium import webdriver
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://opensource-demo.orangehrmlive.com/")

#driver.save_screenshot('C:\Selenium Practice\ScreenShot\homepage.png')
driver.get_screenshot_as_file('C:\Selenium Practice\ScreenShot\homepage2.png')

time.sleep(2)
driver.close()
