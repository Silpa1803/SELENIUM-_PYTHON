from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
time.sleep(3)

admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
userMgnt=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(userMgnt).move_to_element(user).click().perform()

time.sleep(2)
driver.quit()

