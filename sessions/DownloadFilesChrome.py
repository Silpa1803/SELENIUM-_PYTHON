from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#to choose the path for downloaded files
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\Downloads"})

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver',chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(2)

#Text File Download
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("Testing Download Text Files")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click() #Download Link

time.sleep(3)

#PDF File Download
driver.find_element_by_xpath("//*[@id='pdfbox']").send_keys("Testing Download PDF Files")
driver.find_element_by_xpath("//*[@id='createPdf']").click()
driver.find_element_by_xpath("//*[@id='pdf-link-to-download']").click() #Download Link

time.sleep(2)
driver.close()