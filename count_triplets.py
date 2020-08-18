import math
import os
import random
import re
import sys

"""
HackerRank
"""

# Complete the countTriplets function below.
def countTriplets(arr, r):
    val_to_index = dict()
    for i, val in enumerate(arr):
        if val not in val_to_index:
            val_to_index[val] = [i]
        else:
            val_to_index[val].append(i)

    # Works but O(n^3) loop :(
    triplets = []
    for i, val in enumerate(arr):
        next_val = val * r
        if next_val in val_to_index:
            for next_val_i in val_to_index[next_val]:
                if next_val_i > i:
                    next_next_val = next_val * r
                    if next_next_val in val_to_index:
                        for next_next_val_i in val_to_index[next_next_val]:
                            if next_next_val_i > next_val_i:
                                triplets.append([i, next_val_i, next_next_val_i])
    return len(triplets)

arr = [1, 3, 9, 9, 27, 81]
r = 3
print(countTriplets(arr, r))
