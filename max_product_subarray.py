from typing import List

"""
152. Maximum Product Subarray, medium

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Use Dynamic Programming!
        # Subproblems: x(i) = largest product in nums[:i+1] for 0 <= i < len(nums)
        # Relate: x(i) = max{x(i-1)*nums[i], nums[i]}, we have a DAG
        # Base Case: x(-1) = 1
        # Solution: max(x.values())
        # Time: O(n) subproblems, each subproblem is O(1) because finding max, so O(n) total
        # Space: O(n) because creating max_prod and min_prod dictionaries

        max_prod = {0: nums[0]}
        min_prod = {0: nums[0]}
        for i in range(1, len(nums)):
            val = nums[i]
            current_max = max_prod[i-1]
            current_min = min_prod[i-1]
            # Check if current val is positive or negative
            if val > 0:
                min_prod[i] = min(current_min * val, val)
                max_prod[i] = max(current_max * val, val)
            else:
                min_prod[i] = min(current_max * val, val)
                max_prod[i] = max(current_min * val, val)

        return max(max_prod.values()) # Return overall largest product

solution = Solution()
nums = [2, 3, -2, 4]
print("Input nums: ", nums, "\nMax product of subarray: ", solution.maxProduct(nums))
