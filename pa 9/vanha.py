# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 21:45:36 2015

@author: aino
"""

        moves = ''
        zero = [target_row, target_col]
        current_pos = self.current_position(target_tile_pos[0],target_tile_pos[1])
        while current_pos != (target_row, target_col):
            # target in same column
            if current_pos[1] == target_col:
                # zero at top
                if zero[0] < current_pos[0]:
                    self.update_puzzle('lddr')
                    moves += 'lddr'
                    zero[0] += 2
                # zero at below
                elif zero[0] > current_pos[0]:
                    while zero[0] > current_pos[0]:
                        self.update_puzzle('u')
                        moves += 'u'
                        zero[0] -= 1
                # zero at left
                elif zero[1] < current_pos[1]:
                    self.update_puzzle('dru')
                    moves += 'dru'
                    zero[1] += 1
                # zero at right
                else:
                    self.update_puzzle('ullddru')
                    moves += 'ullddru'
                    zero[1] -= 1
                
            # target to left from target column
            elif current_pos[1] < target_col:
                # move up until in same row
                while zero[0] != current_pos[0]:
                    print current_pos
                    print self
                    self.update_puzzle('u')
                    moves += 'u'
                    zero[0] -= 1
                # move left until zero at current, count how many steps
                count = 0
                while zero[1] > current_pos[1]:
                    self.update_puzzle('l')
                    moves += 'l'
                    zero[1] -= 1
                    count += 1
                # if more than 1 step, move more to right
                while count > 1:
                    if zero[0] == 0:
                        self.update_puzzle('drrul')
                        moves += 'drrul'
                        zero[1] += 1 
                        count -= 1
                    else:
                        self.update_puzzle('urrdl')
                        moves += 'urrdl'
                        zero[1] += 1
                        count -= 1
                    
            # target to right from target column
            else:
                # move up until in same row
                print zero, current_pos
                print self
                while zero[0] != current_pos[0]:
                    print zero, current_pos
                    print self
                    self.update_puzzle('u')
                    moves += 'u'
                    zero[0] -= 1
                # move right until zero at 'current', count how many steps taken to right
                count = 0
                while zero[1] < current_pos[1]:
                    self.update_puzzle('r')
                    moves += 'r'
                    zero[1] += 1
                    count += 1
                # if more than 1 step, move more to left
                while count > 1:
                    if zero[0] == 0:
                        self.update_puzzle('dllur')
                        moves += 'dllur'
                        zero[1] -= 1
                        count -= 1
                    else:
                        self.update_puzzle('ulldr')
                        moves += 'ulldr'
                        zero[1] -= 1
                        count -= 1
                    
            current_pos = self.current_position(target_tile_pos[0], target_tile_pos[1])
        # move zero to left from target
        if moves:
            if moves[-1] == 'u':
                self.update_puzzle('ld')
                moves += 'ld'
        return moves
        
        
#########################3
        
    # helper function to move zero
    def move_zero(self, from_tile, to_tile):
        """
        helper function to move only zero, not going into already solved area
        """
        moves = ''
        diff = [to_tile[0] - from_tile[0], to_tile[1] - from_tile[1]]
        # up or down
        if diff[0] < 0: # up
            self.update_puzzle('u' * abs(diff[0]))
            moves += 'u' * abs(diff[0])
        elif diff[0] > 0: # down
            self.update_puzzle('d' * diff[0])
            moves += 'd' * diff[0]
        if diff[1] < 0: # left
            self.update_puzzle('l' * abs(diff[1]))
            moves += 'l' * abs(diff[1])
        elif diff[1] > 0: # right
            self.update_puzzle('r' * diff[1])
            moves += 'r' * diff[1]
        return moves