from selenium import webdriver
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')

driver.get("https://www.facebook.com/")

#capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))     #print numbrt of cookies created
print(cookies)          #print all the cookie pairs

#ADDING NEW COOKIE TO THE BROWSER
cookie={'name':'My Cookie','value':'1234567'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))     #print numbrt of cookies created after adding new cookie
print(cookies)          #print all the cookie pairs

#DELETING COOKIE FILE
driver.delete_cookie('My Cookie')
cookies=driver.get_cookies()
print(len(cookies))     #print numbrt of cookies created after deleting the cookie
print(cookies)          #print all the cookie pairs

#DELETING ALL THE COOKIES
driver.delete_all_cookies()     #deletes all cookies
cookies=driver.get_cookies()    #capture all the cookies after deletes all
print(len(cookies))             #0

time.sleep(3)
driver.close()
