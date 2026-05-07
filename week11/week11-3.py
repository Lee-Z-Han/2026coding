# week11-3.py 學習計畫 Binary Search Tree 第1題 Easy題
# LeetCode 700. Search in a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if root == None: return None 
            if val < root.val: # 小, 在左邊
                return helper(root.left, val)
            if val > root.val: # 大, 在右邊
                return helper(root.right, val)
            if val == root.val: # 剛好相等
                return root # 本身就是答案
        return helper(root, val)