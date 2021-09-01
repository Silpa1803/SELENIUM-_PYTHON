from selenium import webdriver
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("https://chercher.tech/practice/table")
driver.maximize_window()

rows=len(driver.find_elements_by_xpath("//*[@id='webtable']/tbody/tr"))     #count rows in a table
columns=len(driver.find_elements_by_xpath("//*[@id='webtable']/tbody/tr[1]/th"))

print(rows)
print(columns)

print("WEBSITE"+"           "+"TITLE"+"             "+"FIELD")

for r in range(2,rows+1):
    for c in range(1,columns+1):
        value=driver.find_element_by_xpath("//*[@id='webtable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='     ')
    print()
time.sleep(2)
driver.quit()

