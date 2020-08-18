from typing import List

"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each
cell. The distance between two adjacent cells is 1.

Incomplete :( - passed some test cases
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        dist = [[0 if matrix[i][j] == 0 else 100 for j in range(num_cols)] for i in range(num_rows)]

        def helper(matrix, i, j):
            if matrix[i][j] == 0:
                return 0
            else:
                valid_neighbors = []
                if i-1 >= 0:
                    valid_neighbors.append(helper(matrix, i-1, j))
                if j-1 >= 0:
                    valid_neighbors.append(helper(matrix, i, j-1))
                return 1 + min(valid_neighbors)

        for i in range(num_rows):
            for j in range(num_cols):
                dist[i][j] = helper(matrix, i, j)
        return dist

        # Use dynamic programming
        # Subproblems: x(i, j) = min dist to nearest 0 from matrix[i][j] where 0<=i<len(matrix) and 0 <=j<len(matrix[0])
        # Relate: x(i,j) = 1+min(x(i-1,j), x(i+1,j), x(i,j-1), x(i,j+1)), make sure indices are valid and only compare min for non-None values
        # Base case: x(i,j)=0 if matrix[i][j] == 0
        # Solution: x(i,j) for i in len(matrix) and j in len(matrix[i])
        # Time: O(n) where n is number of elements in matrix

matrix = [[0,0,0],
          [0,1,0],
          [1,1,1]]
print(Solution().updateMatrix(matrix))
