# week10-6.py 學習計畫 Binary Tree - DFS 第5題
# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # 整個的答案
        def helper(root):
            if root==None: return 0, 0 # 左邊最長、右邊最長

            Lans1, Lans2 = helper(root.left) # 左邊走, 小朋友的左邊最長、右邊最長
            Rans1, Rans2 = helper(root.right)
            self.ans = max(self.ans, Lans2 + 1, Rans1 + 1)
            return Lans2 + 1, Rans1 + 1
        helper(root)
        return self.ans - 1
