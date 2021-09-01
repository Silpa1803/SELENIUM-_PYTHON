import unittest

class paymentTest(unittest.TestCase):

    def test_paymentInDollar(self):
        print("This is Payment in Dollar test")
        self.assertTrue(True)

    def test_paymentInRupees(self):
        print("This is Payment in Rupees test")
        self.assertTrue(True)

if __name__== "__main__":
    unittest.main()