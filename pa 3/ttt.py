
"""
Created on Mon Sep 14 17:51:41 2015

@author: sakari hakala

Principles of Computing, programming assingment 3
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided



# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    ''' Makes random moves for both players until game ends
    '''
    print 'start------'
    while board.check_win() == None:
        print player
        # choose random empty square
        square = random.choice(board.get_empty_squares())
        # make move with current player
        board.move(square[0], square[1], player)
        # switch player
        player = provided.switch_player(player)
        #print board
        #print '....'
    print 'end--------'
        
def mc_update_scores(scores, board, player):
    ''' upgades running total scores of mc trials
    '''
    winner = board.check_win()
    dim = board.get_dim()
    if winner == provided.DRAW:
        return
    if winner == player:
        calculation = 1
    else:
        calculation = -1
    for row in range(dim):
        for col in range(dim):
            if board.square(row,col) == player:
                scores[row][col] = scores[row][col] + calculation * SCORE_CURRENT
            elif board.square(row,col) == provided.switch_player(player):
                scores[row][col] = scores[row][col] - calculation * SCORE_OTHER
    return

def get_best_move(board, scores):
    ''' finds highest value from scores and return random position with that value
    '''
    max_score = float('-Inf')
    max_score_pos = []
    dim = board.get_dim()
    for row in range(dim):
        for col in range(dim):
            if (row,col) not in board.get_empty_squares():
                continue
            if scores[row][col] == max_score:
                
                max_score_pos.append((row,col))
            elif scores[row][col] > max_score:
                max_score_pos = [(row,col)]
                max_score = scores[row][col]
    #print max_score_pos
    return random.choice(max_score_pos)  

def mc_move(board, player, ntrials):
    ''' calculates ntrial mc trial and returns best move
    '''
    print player
    scores = [[0 for dummy in range(board.get_dim())] for dummy in range(board.get_dim())]   
    if len(board.get_empty_squares()) == 1:
        return board.get_empty_squares().pop()
    
    for dummy in range(ntrials):
        clone = board.clone()
        print player
        mc_trial(clone, player)
        print player
        mc_update_scores(scores, clone, player)
        print player
    print board
    return get_best_move(board, scores)    
       
#import poc_ttt_testsuite as test
#test.run_suite(get_best_move)

#scores = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]

#scores = [[3, 2, 5], [8, 2, 8], [4, 0, 2]]
#print get_best_move(provided.TTTBoard(3), scores)
#
#
#print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                     [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], 
#                                    [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, NTRIALS)

#print get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.PLAYERX], [provided.EMPTY, provided.PLAYERO]]), [[3, 3], [0, 0]])

#print provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                     [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], 
#                                    [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]])
#scores = [[0 for dummy in range(3)] for dummy in range(3)]        
#game = provided.TTTBoard(3)
#
#clone = game.clone()
#mc_trial(clone, provided.PLAYERX)
#mc_update_scores(scores, clone, provided.PLAYERX)
#print clone
#print scores
#
#clone = game.clone()
#mc_trial(clone, provided.PLAYERX)
#mc_update_scores(scores, clone, provided.PLAYERX)
#print scores

#print mc_update_scores(scores, game, provided.PLAYERX)
#print get_best_move(game, scores)
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
