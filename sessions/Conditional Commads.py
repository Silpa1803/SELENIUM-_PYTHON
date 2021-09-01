from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='pageFooter']/ul/li[11]/a").click()

email_ele=driver.find_element_by_xpath("//*[@id='email']")

print(email_ele.is_displayed())  #Conditional command returns T/F based on element status
print(email_ele.is_enabled())  #Conditional command returns T/F

email_ele.send_keys("silpasahoo31@gmail.com")

pwd_ele=driver.find_element_by_xpath("//*[@id='pass']")
pwd_ele.send_keys("@ashishhbkof.")

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]").click()

#print(ele.is_selected())    #returns T/F based on element status

#driver.close()      #close currently focused browser
#driver.quit()      #close all the browsers


