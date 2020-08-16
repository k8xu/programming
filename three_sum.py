from typing import List

"""
15. 3Sum, medium

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        triplets = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                a = nums[i]
                b = nums[j]
                c = 0 - a - b
                if freq[a] == 1 and (a == b or a == c):
                    continue
                if freq[a] == 2 and (a == b and b == c):
                    continue
                if freq[b] == 1 and (b == c):
                    continue
                if freq.get(c, 0) > 0:
                    triplet = [a, b, c]
                    triplet.sort()
                    if triplet not in triplets:
                        triplets.append(triplet)
        return triplets

nums = [-1, 0, 1, 2, -1, -4]
print("Solution: ", Solution().threeSum(nums))
