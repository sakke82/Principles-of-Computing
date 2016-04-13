"""
Created on Tue Oct 27 08:46:00 2015

@author: Sakari Hakala

Principles of Computing, part 2, pa 8
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_provided as provided

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
#    score = 0
#    move = (-1, -1)
#    print board, player
#    # Base case
#    if board.check_win():
#        score = SCORES[board.check_win()]
#        print score, move
#        return score, move
#    
#    # Recursive case
#    best_score = None
#    best_move = None
#    for square in board.get_empty_squares():
#        board_copy = board.clone()
#        player_copy = provided.switch_player(player)
#        board_copy.move(square[0], square[1], player)
#        print square
#        score, move = mm_move(board_copy, player_copy)
#        score = score * SCORES[player]
#        
#        if score == 1:
#            return score, move
#        elif best_score == None or score > best_score:
#            best_score = score
#            best_move = move
#    
#    return best_score, best_move
    
    #print 'NEW CALL!'
    #print board, player
    #score = None
    best_score = -2
    best_move = (-1,-1)
    for square in board.get_empty_squares():
        board_copy = board.clone()
        player_copy = provided.switch_player(player)
        board_copy.move(square[0], square[1], player)
        if board_copy.check_win():
            score = SCORES[board_copy.check_win()] 
            #print 'GAME OVER'
            #print board_copy
            #print score
            return score, square
        move = mm_move(board_copy, player_copy)
        #print move
        score = move[0] #score joka tulee rekursiosta ylempaa
        score_to_max = move[0] * SCORES[player] # kerrottuna playerilla jotta voidaan maxsimoida
        #print score
        if score_to_max == 1: # jos (X ja 1) tai (O ja -1)
            return score, square # palautetaan alkuperainen score ja ruutu
        if score_to_max > best_score: # jos (X ja 0 tai -1) tai (O ja 0 tai 1)
            best_score = score_to_max # 0 tai -1
            best_move = square
            score_to_return = score
    
    return score_to_return, best_move
    

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        


#testboard = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX], [provided.EMPTY, provided.PLAYERO, provided.EMPTY]])
#print mm_move(testboard, provided.PLAYERX)