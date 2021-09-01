#assertEqual and assertNotEqual
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title

        #assertEqual
        #self.assertEqual("Google",titleOfWebpage,"webpage title is not same.")

        #assertNotEqual
        self.assertNotEqual("Google", titleOfWebpage, "webpage title is not same.")

if __name__== "__main__":
    unittest.main()
