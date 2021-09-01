import XLUtils
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

path="C:\Selenium Practice\DataDrivenTestcase.xlsx"

rows=XLUtils.getrowcount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,'Sheet1',r,1)
    password=XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys(username)
    driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys(password)
    driver.find_element_by_xpath("//*[@id='btnLogin']").click()

    if driver.title=="OrangeHRM":
        print("Test is Passed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test Passed")
    else:
        print("Test Failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    element=driver.find_element_by_id("//*[@id='welcome']")
    drp=Select(element)
    drp.select_by_visible_text('Logout')