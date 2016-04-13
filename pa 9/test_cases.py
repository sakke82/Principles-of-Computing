# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 10:58:05 2015

@author: aino
"""

import fifteen_puzzle as fp

#puzzle = fp.Puzzle(3,3)
#puzzle.update_puzzle('ddr')
#print puzzle.lower_row_invariant(2,0) # False
#print puzzle.lower_row_invariant(2,1) # True 
#print puzzle.lower_row_invariant(2,2) # False  
#
#print puzzle.solve_interior_tile(2,1)
#
#print '*********'
#
#puzzle = fp.Puzzle(4,4)
#puzzle.update_puzzle('rrdldruldr')
#print puzzle
#print puzzle.lower_row_invariant(2,2)
#print puzzle.solve_interior_tile(2,2)
#
#print '********'
#
#puzzle = fp.Puzzle(4,4)
#puzzle.update_puzzle('rdddluurdluurddd')
#print puzzle
#print puzzle.lower_row_invariant(3,1)
#print puzzle.solve_interior_tile(3,1)
#
#print '*******'
#puzzle = fp.Puzzle(4,4)
#puzzle.update_puzzle('drdluurrdlurrdlld')
#print puzzle
#print puzzle.lower_row_invariant(2,1)
#print puzzle.solve_interior_tile(2,1)
#
#print '*******'
#obj = fp.Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#print obj
#print obj.solve_interior_tile(2,2)
#
#print '******'
#
#obj = fp.Puzzle(3, 2, [[1,2],[3,4],[0,5]])
#print obj
#print obj.solve_col0_tile(2)
#print obj
#
#print '******'
#
#obj = fp.Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])   
#print obj
#print obj.solve_col0_tile(2)
#
#print '******'
#
#obj = fp.Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]])
#print obj
#print obj.solve_col0_tile(3)
#print obj
#
#print '*****'
#
#obj = fp.Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
#print obj
#print obj.row1_invariant(0)
#print obj.row1_invariant(1)
#print obj.lower_row_invariant(1,1)
#
#print '****'
#
#obj = fp.Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#print obj
#print obj.row0_invariant(0)
#print obj.row1_invariant(0)
#print obj.lower_row_invariant(1,0)
#
#print '******'
#
#obj = fp.Puzzle(3,3,[[2,4,3],[5,1,0],[6,7,8]])
#print obj
#print obj.solve_row1_tile(2)
#print obj
#
#print '******'
#
#obj = fp.Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
#print obj
#print obj.row0_invariant(2)
#print obj.solve_row0_tile(2)
#print obj
#
#print '*****'
#
#obj = fp.Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
#print obj
#print obj.solve_2x2()
#print obj
#
#print '*****'
#
#obj = fp.Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#print obj
#print obj.solve_puzzle()
#print obj
#
#print '*******'

#obj = fp.Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#print obj
##print obj.row0_inva
##print obj.lower_row_invariant(0,0)
#print obj.solve_puzzle()
#
#print '*******'
#
#obj = fp.Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
#print obj
#print obj.solve_puzzle()
#print obj
#
#print '********'
#
#obj = fp.Puzzle(5, 4, [[5, 4, 2, 3], [1, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]])
#print obj
#print obj.solve_puzzle()
#print obj
#
#print '*******'
#
#obj = fp.Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], [3, 0, 14, 10, 12, 6], [4, 15, 2, 11, 8, 1]])
#print obj
#print obj.solve_puzzle()
#print obj
#
#print '******'

puzzle=fp.Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
sol=puzzle.solve_puzzle()
print sol
print len(sol)