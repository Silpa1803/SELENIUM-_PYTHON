#assertIsNone and assertIsNotNone
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        #driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
        #self.assertIsNone(driver)   #testcase Failed
        #self.assertIsNotNone(driver)    #testcase Passed

        driver1=None
        #self.assertIsNone(driver1)      #returns Passed
        self.assertIsNotNone(driver1)   #returns Failed
if __name__== "__main__":
    unittest.main()
