import unittest

def setUpModule(): #will be executed before executing any class or any method present in the test class
    print("setUpModule")

def tearDownModule(): #will be executed after completing everything present in the python module
    print("tearDownModule")

class Apptesting(unittest.TestCase):

    @classmethod
    def setUp(self):        #Executes before all the test methods
        print("This is login test")

    @classmethod
    def tearDown(self):     #Executes after all the test methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls):        #Execute once when the class is started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):     #Execute once after the class is completed
        print("Close Application")

    def test_search(self):
        print("This is Search Test")

    def test_advancedsearch(self):
        print("This is Advanced Search Test")

    def test_prepainRecharge(self):
        print("This is prepaid racharge Test")

    def test_postpainRecharge(self):
        print("This is postpaid racharge Test")

if __name__=="__main__":
    unittest.main()