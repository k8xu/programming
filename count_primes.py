from typing import List
import math

"""
204. Count Primes, easy

Count the number of prime numbers less than a non-negative number, n.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [2]
        for i in range(3, n):
            prime = True
            for j in primes: # Something here could be more efficient?
                if i % j == 0:
                    prime = False
            if prime:
                primes.append(i)
        return len(primes)

print("Solution: ", Solution().countPrimes(10))
