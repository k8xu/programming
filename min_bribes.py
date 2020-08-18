import math
import os
import random
import re
import sys

"""
HackerRank
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
    num_bribes = 0
    invalid = False

    # Check if q is valid
    for i in range(len(q)):
        key = q[i]
        if key - (i+1) > 2:
            invalid = True
            break

    # Use insertion sort to count bribes
    for i in range(1, len(q)):
        key = q[i]
        j = i-1
        while j >= 0 and key < q[j]:
            q[j+1] = q[j]
            j -= 1
            num_bribes += 1
        q[j+1] = key

    if invalid:
        print("Too chaotic")
    else:
        print(num_bribes)

q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)
