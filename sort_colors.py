from typing import List

"""
75. Sort Colors, medium

Given an array with n objects colored red, white or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red,
white and blue. Here, we will use the integers 0, 1, and 2 to represent the
color red, white, and blue respectively. Note: You are not suppose to use the
library's sort function for this problem.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        index = 0
        for key in sorted(freq.keys()):
            val = freq[key]
            for i in range(val):
                nums[index] = key
                index += 1

        return nums

print("Solution: ", Solution().sortColors([2,0,2,1,1,0]))
