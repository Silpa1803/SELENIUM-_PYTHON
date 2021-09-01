#assertIn and assertNotIn
import unittest

class Test(unittest.TestCase):
    def testName(self):
        list={"python","selenium","java"}

        self.assertIn("python",list)    #passed
        self.assertIn("Ruby", list)     #failed

        #self.assertNotIn("python",list)    #failed
        #self.assertNotIn("Ruby",list)      #passed

if __name__== "__main__":
    unittest.main()
