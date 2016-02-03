# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
    	self.assertEqual(utils.fact(0) , 3)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,5,8), (0,9/1,3/4))
    
    def test_integrate(self):
    	self.assertEqual(utils.integrate(x,4,1), 3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())