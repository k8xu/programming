from typing import List

"""
563. Binary Tree Tilt, easy

Given a binary tree, return the tilt of the whole tree. The tilt of a tree node
is defined as the absolute difference between the sum of all left subtree node
values and the sum of all right subtree node values. Null node has tilt 0. The
tilt of the whole tree is defined as the sum of all nodes' tilt.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt = []
        def helper(root, tilt):
            left = root.left
            right = root.right
            if left is None and right is None:
                tilt.append(0)
            elif right is None:
                tilt.append(left.val) # Need to sum values of nodes in left subtree
            elif left is None:
                tilt.append(right.val)
            else:
                tilt.append((right.val + helper(right, tilt)[-1]) - (left.val + helper(left, tilt)[-1]))
            return tilt
        tilt = helper(root, tilt)
        return sum(tilt)

# root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
# root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4)), right=TreeNode(val=3, left=TreeNode(val=5)))
#           1     tilts = [8-6=2]
#        2    3   tilts = [4, 5]
#     4   N  5    tilts = [0, 0]
root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)))
#           1     tilts = [9]
#        2    N   tilts = [1, 0]
#     3   4       tilts = [0, 0]
print("Solution: ", Solution().findTilt(root))
