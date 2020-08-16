from typing import List

"""
279. Perfect Squares, medium

Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, int(n**0.5)+1):
            squares.append(i * i)

        def helper(n, squares):
            # Similar to coin change problem, use dynamic programming
            min_squares = dict()
            for square in squares:
                min_squares[square] = 1
            for i in range(1, n+1):
                if i in min_squares:
                    continue
                potential = []
                for j in range(len(squares)): # [1, 4, 9]
                    if i - squares[j] >= 0:
                        potential.append(min_squares[i-squares[j]])
                if len(potential) > 0:
                    min_squares[i] = 1 + min(potential)

            return min_squares[n]
        return helper(n, squares)

print("Solution: ", Solution().numSquares(12))
