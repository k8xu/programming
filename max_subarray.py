from typing import List

"""
53. Maximum Subarray, easy

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Success
Runtime: 76 ms, faster than 48.24% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15.7 MB, less than 5.12% of Python3 online submissions for Maximum Subarray.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use dynamic programming
        # Subproblems: x(i) = max subarray sum in nums[:i+1], 0 <= i < len(nums)
        # Relate: x(i) = max(nums[i], x(i-1)+nums[i])
        # Base Case: x(0) = nums[0]
        # Solution: max(x(i)) for i in range(len(nums))
        # Time: O(n) where n = len(nums) because we have a DAG
        # Space: O(n) because we store subproblems

        max_sum = dict()
        max_sum[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum[i] = max(nums[i], max_sum[i-1]+nums[i])
        return max(max_sum.values())

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Solution: ", Solution().maxSubArray(nums))
