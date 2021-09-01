import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
from Package2.TC_PaymentTest import paymentTest
from Package2.TC_PaymentReturnsTest import paymentReturnTest

#Get all the tests from LoginTest, SignupTest, paymentTest and paymentReturnTest:

TC1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
TC4=unittest.TestLoader().loadTestsFromTestCase(paymentReturnTest)

#creating TestSuits:

sanityTestSuite=unittest.TestSuite([TC1,TC2]) #sanity Test Suite

functionalTestSuite=unittest.TestSuite([TC3,TC4]) #functional Test Suite

masterTestSuite=unittest.TestSuite([TC1,TC2,TC3,TC4])  #master Test Suite

#unittest.TextTestRunner().run(sanityTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)