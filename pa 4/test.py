# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:42:09 2015

@author: aino
"""

def left_to_choose(hand, chosen):
    hand = list(hand)
    chosen = list(chosen)
    for item in chosen:
        hand.remove(item)
    return hand

def gen_all_holds(hand):

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

import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)
