from typing import List

"""
55. Jump Game, medium

Given an array of non-negative integers, you are initially positioned at the
first index of the array. Each element in the array represents your maximum jump
length at that position. Determine if you are able to reach the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] >= len(nums)-1:
            return True
        # Dynamic programming
        # Subproblems: x(i) = True if you can reach last index from index i,
        #              otherwise False, 0 <= i < len(nums)
        # Relate: x(i) = True if any x(j) is True, where i+1 <= j <= i+nums[i]
        # Bast Case: x(len(nums)-1) = True
        # Solution: x(0)
        # Time: O(kn) where k is upper bound on values in nums, and n is size of nums
        # Space: O(n)
        reachable = dict()
        reachable[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            reachable[i] = False
            for j in range(i+1, i+nums[i]+1):
                if j < len(nums) and reachable[j]:
                    reachable[i] = True
                    break

        return reachable[0]

nums = [2, 3, 1, 1, 4]
print("Nums: ", nums, "\nSolution: ", Solution().canJump(nums))
