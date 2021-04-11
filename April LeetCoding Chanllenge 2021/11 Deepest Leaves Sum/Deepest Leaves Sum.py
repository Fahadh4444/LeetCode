# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        arr = []

        def sumOfLeaves(node: TreeNode, depth: int):
            if(node):
                if(len(arr) == depth):
                    arr.append(node.val)
                else:
                    arr[depth] = arr[depth] + node.val
                sumOfLeaves(node.left, depth+1)
                sumOfLeaves(node.right, depth+1)
        sumOfLeaves(root, 0)
        return arr[-1]
