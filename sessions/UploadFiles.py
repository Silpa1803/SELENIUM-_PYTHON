from selenium import webdriver
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("http://demo.guru99.com/test/upload/")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_name("uploadfile_0").send_keys("E:/SOFTWARE TESTING/download.jpg")

time.sleep(2)
driver.quit()

