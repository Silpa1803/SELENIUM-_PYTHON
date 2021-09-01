import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest    #decorator
    def test_search(self):
        print("This is Search Test")

    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_advancedsearch(self):
        print("This is Advanced Search Test")

    @unittest.skipIf(1==1,"Numbers are Not Equal")
    def test_prepainRecharge(self):
        print("This is prepaid racharge Test")

    def test_postpainRecharge(self):
        print("This is postpaid racharge Test")

    def test_loginbygmail(self):
        print("This is login by gmail test")

    def test_loginbytwitter(self):
        print("This is login by Twitter test")

if __name__== "__main__":
    unittest.main()