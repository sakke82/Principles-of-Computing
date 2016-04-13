# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:06:23 2015

@author: aino
"""

import ttt_minimax as ttt
import poc_ttt_provided as provided

print ttt.mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], 
                                               [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], 
                                                [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), 
                                                provided.PLAYERX)
                                                
print ttt.mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.PLAYERX], 
                                               [provided.EMPTY, provided.EMPTY, provided.EMPTY], 
                                                [provided.EMPTY, provided.EMPTY, provided.EMPTY]]), 
                                                provided.PLAYERO)                                        
                                                
print ttt.mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
                                               [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], 
                                                [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), 
                                                provided.PLAYERO)
                                                
print ttt.mm_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], 
                                               [provided.EMPTY, provided.EMPTY]]), 
                                                provided.PLAYERX)                                                