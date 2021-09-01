from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")
driver.maximize_window()
time.sleep(2)

element=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)
time.sleep(2)

#select_by_visible_text
drp.select_by_visible_text('Evening')   #select moring

#select_by_index
#drp.select_by_index('2')        #select Afternoon

#select_by_value
#drp.select_by_value("Radio-2")        #select Afternoon


#Count number of options
print(len(drp.options))       #return no. of options present in the drop down

#Capture all the options and print them as output
all_options=drp.options
for option in all_options:
    print(option.text)

time.sleep(2)
driver.close()