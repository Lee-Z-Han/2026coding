# week10-3.py 學習計畫 Binary Tree 第3題
# LeetCode 1448. Count Good Nodes in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,big): # 記得祖先最大的big
            if root==None: return 0 # 提早結束
            ans = 0
            if root.val >= big: 
                ans += 1
                big = root.val
            ans += helper(root.left, big)
            ans += helper(root.right, big)
            return ans
        return helper(root, root.val)