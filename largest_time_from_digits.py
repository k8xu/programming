from typing import List

"""
Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
00:00, a time is larger if more time has elapsed since midnight. Return the
answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""

Note:
A.length == 4
0 <= A[i] <= 9
"""

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # Make frequency dictionary of numbers in A
        freq = dict()
        for num in range(0, 10):
            freq[num] = 0
        for num in A:
            freq[num] += 1

        # Edge cases
        if freq[0] == 0 and freq[1] == 0 and freq[2] == 0:
            return ""
        if freq[3] > 3 or freq[4] > 3 or freq[5] > 3:
            return ""
        if freq[6] > 2 or freq[7] > 2 or freq[8] > 2 or freq[9] > 2:
            return ""
        if freq[2] == 1 and freq[0] == 0 and freq[1] == 0 and freq[3] == 0:
            return ""

        # Find time permutations
        def find_permutations(A):
            if len(A) == 0:
                return []
            if len(A) == 1:
                return [A]
            permutations = []
            for i in range(len(A)):
                m = A[i]
                remaining = A[:i] + A[i+1:]
                remain_perms = find_permutations(remaining)
                for p in remain_perms:
                    new = [m] + p
                    permutations.append(new)
            return permutations
        permutations = find_permutations(A)

        # Sort time permutations and find largest valid time
        perm_int = []
        for i, perm in enumerate(permutations):
            perm_int.append(1000*perm[0] + 100*perm[1] + 10*perm[2] + perm[3])
        perm_int.sort(reverse=True)
        for perm in perm_int:
            if 0 <= perm < 2400:
                perm_str = str(perm)
                return f"{perm_str[:2]}:{perm_str[2:]}"

print(Solution().largestTimeFromDigits([1, 2, 3, 4]))
