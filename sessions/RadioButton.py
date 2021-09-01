from selenium import webdriver
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")
time.sleep(3)   #from Python

#Working with Radio Buttons

status=driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']").is_selected()   #true/false
print(status)

#driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']").click()         #select radio button

#status=driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']").is_selected()
#print(status)

#Working with Check Box

driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_0']").click()
driver.find_element_by_id("RESULT_CheckBox-8_2").click()
driver.close()