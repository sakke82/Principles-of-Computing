"""
Created on Fri Oct 23 09:09:02 2015

@author: Sakari Hakala

Principles of Computing, part 2, miniproject 2
Ordered lists and recursion

Student code for Word Wrangler game
"""

#import urllib2
#import codeskulptor
#import poc_wrangler_provided as provided
import math

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    last = None
    for item in list1:
        if item != last:
            new_list.append(item)
        last = item
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersect_list = []
    list1_copy = list(list1)
    list2_copy = list(list2)
    while list1_copy and list2_copy:
        if list1_copy[0] == list2_copy[0]:
            intersect_list.append(list1_copy[0])
            list1_copy = list1_copy[1::]
            list2_copy = list2_copy[1::]
        elif list1_copy[0] < list2_copy[0]:
            list1_copy = list1_copy[1::]
        else:
            list2_copy = list2_copy[1::]
    
    return intersect_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    merge_list = []
    list1_copy = list(list1)
    list2_copy = list(list2)
    
    while list1_copy or list2_copy:
        if not list1_copy:
            merge_list.append(list2_copy.pop(0))
        elif not list2_copy:
            merge_list.append(list1_copy.pop(0))
        else:
            if list1_copy[0] <= list2_copy[0]:
                merge_list.append(list1_copy.pop(0))
            else:
                merge_list.append(list2_copy.pop(0))
    return merge_list
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # Base case
    if len(list1) < 2:
        return list1
    # Recursion
    middle = int(math.floor(len(list1) /2))
    left = list1[:middle]
    right = list1[middle:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    list1_sorted = merge(left_sorted, right_sorted)
    return list1_sorted

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """

    if len(word) <= 1:
        if word == '':
            return ['']
        return ['',word]
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    string_list = list(rest_strings)
    #string_list.append(first)
    for string in rest_strings:
        for idx in range(len(string)+1):
            start = string[:idx]
            end = string[idx:]
            new_word = start + first + end
            string_list.append(new_word)
           
        
    return string_list

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    with open("assets_scrabble_words3.txt",'r') as words:
        data = words.readlines()
    return data

#def run():
#    """
#    Run game.
#    """
#    words = load_words(WORDFILE)
#    wrangler = provided.WordWrangler(words, remove_duplicates, 
#                                     intersect, merge_sort, 
#                                     gen_all_strings)
#    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()

    
    
