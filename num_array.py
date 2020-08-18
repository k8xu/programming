from typing import List

"""
Given an integer array nums, find the sum of the elements between indices
i and j (i ≤ j), inclusive. The update(i, val) function modifies nums by
updating the element at index i to val.

Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Constraints:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
0 <= i <= j <= nums.length - 1
"""

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for index in range(i, j+1):
            sum += self.nums[index]
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
