# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:49:35 2015

@author: aino

Principles of Computing, programming assignment 4
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

import poc_yatzee_testsuite

def left_to_choose(hand, chosen):
    ''' returns list of dice not yet chosen
    '''
    hand = list(hand)
    chosen = list(chosen)
    for item in chosen:
        hand.remove(item)
    return hand 

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    best_score = 0
    for value in hand:
        temp_score = 0
        for dice in hand:
            if dice == value:
                temp_score += value
        if temp_score > best_score:
            best_score = temp_score
    return best_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    all_seqs = gen_all_sequences(range(1,num_die_sides+1), num_free_dice)
    count = float(len(all_seqs))
    total_score = 0
    for seq in all_seqs:
        total_score += score(tuple(list(held_dice) + list(seq)))
    return total_score / count

print expected_value((3,3),8,5)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = set([()])
    for dummy_length in range(len(hand)):
        temp_set = set()
        for partial_seq in all_holds:
            for item in left_to_choose(hand, partial_seq):
                new_seq = list(partial_seq)
                new_seq.append(item)
                temp_set.add(tuple(sorted(new_seq)))
        all_holds.update(temp_set)

    return all_holds

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    best_hold = None
    best_expected = 0
    for hold in gen_all_holds(hand):
        expected = expected_value(hold, num_die_sides, (len(hand)-len(hold)))
        if expected > best_expected:
            best_expected = expected
            best_hold = hold
    
    return (best_expected, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score    
    
#run_example()
poc_yatzee_testsuite.run_suite(gen_all_holds)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    





