# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:25:10 2015

@author: aino
"""

import wrangler

l1 = [1, 2, 4, 6,9,11]
l2 = [1,3, 4, 11]

print wrangler.intersect(l1,l2)

print wrangler.merge(l1,l2)

l3 = [3, 6,2,8,9,5,11,1,3]
l4 = [3,1]

l5 = [3]
l6 = [1]

l7 = ['a', 'aa', 'hh', 'ha', 'aab']

print wrangler.merge(l5,l6)

print wrangler.merge_sort(l7)

words = wrangler.gen_all_strings('')

print wrangler.remove_duplicates([1,3,3,8])