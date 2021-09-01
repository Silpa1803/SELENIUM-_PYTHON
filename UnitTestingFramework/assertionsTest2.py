#assertTrue and assertFalse
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title

        #assertTrue
        #self.assertTrue(titleOfWebpage == 'Google12') #True

        #assertFalse
        self.assertFalse(titleOfWebpage=='Google46') #False

if __name__== "__main__":
    unittest.main()
