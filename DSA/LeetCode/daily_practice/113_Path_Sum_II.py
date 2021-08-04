# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """Depth-first Search."""
        # Edge case
        if root is None:
            return []

        # Initialization
        explored = set()  # id of nodes that have been explored
        sta = deque([root])
        path_sum = root.val
        paths = []  # Result
        while sta:
            top = sta[-1]
            left, right = top.left, top.right
            if left is not None and id(left) not in explored:
                sta.append(left)
                path_sum += left.val
            elif right is not None and id(right) not in explored:
                sta.append(right)
                path_sum += right.val
            else:
                if left is None and right is None and path_sum == targetSum:
                    paths.append(list(map(lambda node: node.val, sta)))
                explored.add(id(sta.pop()))
                path_sum -= top.val
        
        return paths
