# week10-2a.py 學習計畫 Binary Tree - DFS 第1題
# LeetCode 104. Maximum Depth of Binary Tree
# DFS 深度優先搜尋 tree最喜歡用「函式呼叫函式」來解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None: return 0 # 沒有東西, 深度是0
            left = helper(root.left) # 左邊的深度
            right = helper(root.right) # 右邊的深度
            return max(left, right) + 1
        return helper(root)