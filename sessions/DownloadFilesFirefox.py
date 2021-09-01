from selenium import webdriver
import time

fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")    #mine type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C:\Downloads")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver=webdriver.Firefox(r'C:\Users\silpa\PycharmProjects\firefoxdriver\Firefox',firefox_profile=fp)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(2)

#Text File Download
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("Testing Download Text Files")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click() #Download Link

time.sleep(3)

#PDF File Download
#driver.find_element_by_xpath("//*[@id='pdfbox']").send_keys("Testing Download PDF Files")
#driver.find_element_by_xpath("//*[@id='createPdf']").click()
#driver.find_element_by_xpath("//*[@id='pdf-link-to-download']").click() #Download Link

#time.sleep(2)
driver.close()