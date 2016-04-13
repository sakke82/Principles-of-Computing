"""
Created on Thu Nov 05 10:56:27 2015

Principles of Computing, part 2

@author: Sakari Hakala

Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # zero in right place
        if self._grid[target_row][target_col] != 0:
            return False
        # all to to the right 
        for col in range(target_col+1, self._width):
            if self._grid[target_row][col] != self._width * target_row + col:
                return False
        # all lower rows
        for row in range(target_row +1, self._height):
            for col in range(0,self._width):
                if self._grid[row][col] != self._width * row + col:
                    return False
        return True
    

            
    # helper function to move tiles
    def position_tile(self, target_tile_pos, zero, target_row, target_col):
        """
        Moves target_tile to position (to_row, to_col) with zero tile 
        position with list [zero_row, zero_col].
        Returns moves as a string
        """
        moves = ''
        #zero = [target_row, target_col]
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
                    if zero[0] == 0:
                        self.update_puzzle('dlu')
                        moves += 'dlu'
                        zero[1] -= 1
                    else:
                        self.update_puzzle('ullddru')
                        moves += 'ullddru'
                        zero[1] -= 1
                
            # target to left from target column
            elif current_pos[1] < target_col:
                # move up until in same row
                while zero[0] != current_pos[0]:
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
                while zero[0] != current_pos[0]:
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

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        moves = self.position_tile([target_row, target_col], [target_row, target_col], target_row, target_col)
        assert self.lower_row_invariant(target_row, target_col - 1), "lower_row_invariant is false" + str(self._grid)
        return moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # if target right above
        if self.current_position(target_row,0) == (target_row-1, 0):
            self.update_puzzle('u')
            moves = 'u'
            for _dummy in range(self._width -1):
                self.update_puzzle('r')
                moves += 'r'
            return moves
        self.update_puzzle('u')
        moves = 'u'
        zero = [target_row -1, 0]

        moves += self.position_tile([target_row,0], zero, target_row-1,1)    
        # rotate with above line being [zero, target]
        self.update_puzzle('ruldrdlurdluurddlur')
        moves += 'ruldrdlurdluurddlur'
        # move zero to last tile at right
        self.update_puzzle('r' * (self._width -2))
        moves += 'r' * (self._width -2)
        assert self.lower_row_invariant(target_row -1, self._width -1), " invariant failure"
        return moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Check zero
        if self._grid[0][target_col] != 0:
            return False
        # Check row 0 from column target_col+1
        for col in range(target_col +1, self._width):
            if self._grid[0][col] != col:
                return False
        # Check row 1 to right
        for col in range(target_col, self._width):
            if self._grid[1][col] != self._width + col:
                return False
        # Check lower rows
        for row in range(2, self._height):
            for col in range(0,self._width):
                if self._grid[row][col] != self._width * row + col:
                    return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Check zero
        if self._grid[1][target_col] != 0:
            return False
        # Check row 0 from column target_col+1
        for col in range(target_col +1, self._width):
            if self._grid[0][col] != col:
                return False
        # Check row 1 to right
        for col in range(target_col+1, self._width):
            if self._grid[1][col] != self._width + col:
                return False
        # Check lower rows
        for row in range(2, self._height):
            for col in range(0,self._width):
                if self._grid[row][col] != self._width * row + col:
                    return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col), "row0_invariant error"
        
        self.update_puzzle('ld')
        moves = "ld"
        zero = [1, target_col -1]
        current_pos = self.current_position(0, target_col)
        if current_pos == (0, target_col):
            return moves
        # move target_tile 
        while current_pos != (1, target_col -1):
            # if target_tile in row 0
            if current_pos[0] == 0:
                if zero[0] == 0:
                    self.update_puzzle('d')
                    moves += 'd'
                    zero[0] += 1
                while zero[1] != current_pos[1]:
                    self.update_puzzle('l')
                    moves += 'l'
                    zero[1] -= 1
                self.update_puzzle('u')
                moves += 'u'
                zero[0] -= 1
            # if target_tile in row1
            else:
                if zero[1] == current_pos[1] -1:
                    self.update_puzzle('urrdl')
                    moves += 'urrdl'
                    zero[1] += 1
                elif zero == [0, current_pos[1]]:
                    self.update_puzzle('rdl')
                    moves += 'rdl'
                    zero[0] += 1
                else: 
                    self.update_puzzle('l')
                    moves += 'l'
                    zero[1] -= 1
            print self
            current_pos = self.current_position(0, target_col)
        print self
        if zero == [0,target_col -1]:
            self.update_puzzle('ld')
            moves += 'ld'
            zero[0] -= 1
            zero[1] += 1
        self.update_puzzle('urdlurrdluldrruld')
        moves += 'urdlurrdluldrruld'
        assert self.row1_invariant(target_col -1), "row1 invariant"
        return moves

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col), "row1_invariant error"
        moves = ''
        zero = [1, target_col]
        current_pos = self.current_position(1,target_col)
        while current_pos != (1,target_col):
            # if target on row1
            if current_pos[0] == 1:
                # if zero on row1
                if zero[0] == 1:
                    self.update_puzzle('u')
                    moves += 'u'
                    zero[0] -= 1
                while zero[1] != current_pos[1]:
                    self.update_puzzle('l')
                    moves += 'l'
                    zero[1] -= 1
                self.update_puzzle('d')
                moves += 'd'
                zero[0] += 1
            
            # if target is on upper tile
            elif current_pos == (0, target_col):
                # move zero to row1
                if zero[0] == 0:
                    self.update_puzzle('d')
                    moves += 'd'
                    zero[0] += 1
                # move zero to target_col
                while zero[1] != target_col: 
                    self.update_puzzle('r')
                    moves += 'r'
                    zero[1] += 1
                self.update_puzzle('u')
                moves += 'u'
                zero[0] -= 1
            # target on row0 and col left from target_col
            else:
                if zero[0] == 1:
                    if zero[1] == current_pos[1]:
                        self.update_puzzle('r')
                        moves += 'r'
                        zero[1] += 1
                    self.update_puzzle('u')
                    moves += 'u'
                    zero[0] -= 1
                # zero on left side of target_tile    
                elif zero[1] == current_pos[1] -1:
                    self.update_puzzle('drrul')
                    moves += 'drrul'
                    zero[1] += 1
                while zero[1] != current_pos[1]:
                    self.update_puzzle('l')
                    moves += 'l'
                    zero[1] -= 1
            current_pos = self.current_position(1,target_col)
        assert self.row0_invariant(target_col), "row0_invariant error" 
        return moves

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1), " row1_invariant error"
        moves = ""
        current_pos = self.current_position(1,1)
        while current_pos != (1,0):
            self.update_puzzle('lurd')
            moves += 'lurd'
            current_pos = self.current_position(1,1)
        self.update_puzzle('lu')
        moves += 'lu'
            
        return moves

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        zero = list(self.current_position(0,0))
        print self
        print 'zero:', zero
        moves = ""
        ready_to_start = False
        # find right spot to start
        while not ready_to_start:
            if zero == [0,0]:
                ready_to_start = self.lower_row_invariant(0,0)
            elif zero[0] == 1:
                ready_to_start = self.row1_invariant(zero[1])
            elif zero[0] == 0:
                ready_to_start = self.row0_invariant(zero[1])
            ready_to_start = self.lower_row_invariant(zero[0],zero[1])
            if not ready_to_start:
                if zero[1] == self._width -1:
                    self.update_puzzle('l' * (self._width-1) + 'd' )
                    moves += 'l' * (self._width-1) + 'd'
                    zero[1] = 0
                    zero[0] += 1
                else:
                    self.update_puzzle('r')
                    moves += 'r'
                    zero[1] += 1

        print 'zero: ', zero
        print 'phase 1'
        print self
        if zero[0] > 1:
            for row in range(zero[0], 1, -1):
                for col in range(zero[1], -1, -1):
                    zero[1] = self._width -1
                    if col == 0:
                        moves += self.solve_col0_tile(row)
                    else:   
                        moves += self.solve_interior_tile(row,col)
        print 'phase 2'
        print self
        zero = list(self.current_position(0,0))
        print 'zero: ', zero
        if zero[0] == 1:
            last_two_rows = min(self._width -1, zero[1])
            while last_two_rows != 1:
                moves += self.solve_row1_tile(last_two_rows)
                moves += self.solve_row0_tile(last_two_rows)
                last_two_rows -= 1
        print 'phase 3'
        print self
        if self.row1_invariant(1):
            moves += self.solve_2x2()
        return moves

# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4,4))


