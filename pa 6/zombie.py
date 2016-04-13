# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:24:28 2015

Principles of Computing (Part 2),
programming assignment 5, Zombie Apocalypse
https://class.coursera.org/principlescomputing2-004/wiki/view?page=zombie

Author: Sakari Hakala

Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
#import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in  self._human_list:
            yield human
        return
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        
        height = poc_grid.Grid.get_grid_height(self)
        widht = poc_grid.Grid.get_grid_width(self)
        visited = [[EMPTY for dummy in range(widht)] for dummy in range(height)]
        distance_field = [[widht * height for dummy in range(widht)] for dummy in range(height)]
        queue = poc_queue.Queue()
        if entity_type == ZOMBIE:
            use_list = self._zombie_list
        else:
            use_list = self._human_list
        for item in use_list:
            queue.enqueue(item)
            visited[item[0]][item[1]] = FULL
            distance_field[item[0]][item[1]] = 0
        while queue:
            current_cell = queue.dequeue()
            neighbors = poc_grid.Grid.four_neighbors(self, current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    if not visited[neighbor[0]][neighbor[1]]:
                        queue.enqueue(neighbor)
                        distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] +1
                        visited[neighbor[0]][neighbor[1]] = FULL
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_humans = []
        zombie_distance_field = self.compute_distance_field(ZOMBIE)
        for human in self.humans():
            moves = poc_grid.Grid.eight_neighbors(self,human[0],human[1])
            moves.append(human)
            max_dist = -1
            max_dist_move = []
            for move in moves:
                if poc_grid.Grid.is_empty(self, move[0], move[1]):
                    dist = zombie_distance_field[move[0]][move[1]]
                    if dist > max_dist:
                        max_dist = dist
                        max_dist_move = [move]
                    elif dist == max_dist:
                        max_dist_move.append(move)
            if len(max_dist_move) > 1:
                make_move = random.choice(max_dist_move)
            else:
                make_move = max_dist_move[0]
            new_humans.append(make_move)
        self._human_list = new_humans
            
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombies = []
        human_distance_field = self.compute_distance_field(HUMAN)
        for zombie in self.zombies():
            moves = poc_grid.Grid.four_neighbors(self, zombie[0], zombie[1])
            moves.append(zombie)
            min_dist = poc_grid.Grid.get_grid_height(self) * poc_grid.Grid.get_grid_width(self)
            min_dist_move = []
            for move in moves:
                if poc_grid.Grid.is_empty(self, move[0], move[1]):	
                    dist = human_distance_field[move[0]][move[1]]
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_move = [move]
                    elif dist == min_dist:
                        min_dist_move.append(move)
            make_move = random.choice(min_dist_move)
            new_zombies.append(make_move)
        self._zombie_list = new_zombies
                

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))
#game = Apocalypse(30,40)
#game.compute_distance_field('human')

obj = Apocalypse(3, 3, [], [(1, 1)], [])
print obj.compute_distance_field(ZOMBIE) 