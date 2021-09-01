#Relational comparison
import unittest

class Test(unittest.TestCase):
    def testName(self):
        #self.assertGreater(100,10)  #Passed
        #self.assertGreater(20, 200)     #failed

        #self.assertGreaterEqual(200, 200)     #passed
        #self.assertGreaterEqual(500, 200)      #passed
        #self.assertGreaterEqual(100, 200)       #failed

        #self.assertLess(10,100)          #Passed
        #self.assertLess(200, 20)         #failed

        #self.assertLessEqual(100,100)          #Passed
        #self.assertLessEqual(10,100)          #Passed
        self.assertLessEqual(200, 20)     # failed

if __name__== "__main__":
    unittest.main()
