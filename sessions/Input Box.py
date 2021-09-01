from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")
time.sleep(3)   #from Python

#How to findout the number of input boxes present in the webpage

input_boxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(input_boxes))


driver.find_element_by_name("RESULT_TextField-1").send_keys("Silpa")
driver.find_element_by_name("RESULT_TextField-2").send_keys("Sahoo")
driver.find_element_by_name("RESULT_TextField-3").send_keys("6362602659")
driver.find_element_by_name("RESULT_TextField-4").send_keys("6362602659")
driver.find_element_by_name("RESULT_TextField-5").send_keys("6362602659")
driver.find_element_by_name("RESULT_TextField-6").send_keys("6362602659")



driver.close()