from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(2)

source_ele=driver.find_element_by_xpath("//*[@id='box4']")
target_ele=driver.find_element_by_xpath("//*[@id='box106']")

actions=ActionChains(driver)
actions.drag_and_drop(source_ele,target_ele).perform() #perform Drag and Drop

time.sleep(2)
driver.quit()

