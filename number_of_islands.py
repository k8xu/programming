from typing import List

"""
200. Number of Islands, medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # In progress
        return

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]
print("Solution: ", Solution().numIslands(grid))
