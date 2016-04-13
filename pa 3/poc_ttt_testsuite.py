# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:21:14 2015

@author: aino
"""

import poc_simpletest
import poc_ttt_provided as provided


def run_suite(get_best_move):
    '''
    '''
    
    suite = poc_simpletest.TestSuite()
    
    # test #1, OK get best move didnt check if the square was empty,
    suite.run_test(get_best_move(provided.TTTBoard(2, False, 
                                                   [[provided.EMPTY, provided.PLAYERX], 
                                                    [provided.EMPTY, provided.PLAYERO]]), 
                                                    [[3, 3], [0, 0]]), (0,0), "Test #1")
                                
    # test #2,
#    suite.run_test(mc_move(provided.TTTBoard(3, False, 
#                            [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], 
#                             [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], 
#                            [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), 
#                            provided.PLAYERO, NTRIALS), )
#    
    #returned mostly bad moves: [(1, 1), (1, 1), (1, 1), (1, 0), (1, 1)]
    suite.run_test(get_best_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
                                               [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], 
                                               [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), 
                                                [[0, 2, 0], [0, 2, 0], [0, 2, 0]]), (2,1), "Test #3") 
    #expected one tuple from [(2, 1)] but received (Exception: IndexError) "list index out of range" at line 274, in choice
    #return seq[int(self.random() * len(seq))]  # raises IndexError if seq is empty