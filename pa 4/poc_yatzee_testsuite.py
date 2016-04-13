# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:21:14 2015

@author: aino
"""

import poc_simpletest

#
#def run_suite(score):
#    '''
#    '''
#    
#    suite = poc_simpletest.TestSuite()
#    
#    suite.run_test(score((5, 6)), 6, '# Test 1')
#    suite.run_test(score((3, 2)), 3, '# Test 2')
#    suite.run_test(score((5, 6, 5)), 10, '# Test 3')
#    suite.run_test(score((5, 6, 4, 4)), 8, '# Test 4')
#    suite.run_test(score((5, 6, 6, 1)), 12, '# Test 5')
#    suite.run_test(score((5, 6, 2, 2, 2)), 6, '# Test 6')
#
#    #suite.run_test()

def run_suite(gen_all_holds):
    '''
    '''
    
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(gen_all_holds(()), set([()]), 'Empty hand')
    suite.run_test(gen_all_holds((1,)), set([(),(1,)]), 'One dice')
    suite.run_test(gen_all_holds((1,2)), set([(),(1,),(2,),(1,2)]), 'Two different dice')
    suite.run_test(gen_all_holds((1,1)), set([(),(1,),(1,1)]) , 'Two same dice')
    suite.run_test(gen_all_holds((1,2,3)), set([(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)]), 'Three diff dice')
    suite.run_test(gen_all_holds((1,1,2)), set([(),(1,),(2,),(1,1),(1,2),(1,1,2)]), '3/2 diff dice')
    suite.run_test(gen_all_holds((1,1,1)), set([(),(1,),(1,1),(1,1,1)]), 'Three same dice')
    