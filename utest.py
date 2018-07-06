#Author: Andy Cui
#Environment: python 3.7.0
#Content: test use unittest to test the basic calculate function
import unittest
import sys

def add(a, b):
    return(a+b)
def sub(a, b):
	return(a-b)
def mul(a, b):
	return(a*b)
def div(a, b):
	return(a/b)

class demoTest(unittest.TestCase):
	#adder function 
    def test_add_4_5(self): 
        self.assertEqual(add(4, 5), 9) #example for correct test
    #subtracter function
    def test_sub_4_5(self):
    	self.assertEqual(sub(4, 5), 9) #example for error test

    #multiplier function
    def test_mul_4_5(self):
    	self.assertEqual(mul(4, 5), 8) #example for error test
    #divider function
    def test_div_4_5(self): #example for correct test
    	self.assertEqual(div(4, 5), 0.8)
if __name__=='__main__':
    unittest.main()