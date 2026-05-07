# week11-4.py 學習計畫 Binary Search Tree 最後1題
# LeetCode 450. Delete Node in a BST 把某個node殺掉, 再找到繼承者, 放在格子裡
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root): # 找到最右邊那個人
            if root.right: # 右邊還有! 
                return findRightest(root.right) # 繼續往右邊走
            return root # 沒有右邊, 那就「你」自己上

        if root == None: return root 
        if root.val == key: 
            # root.val = 999 # 代表要殺
            if root.left:
                now = findRightest(root.left) # 找到繼承者 now
                root.val = now.val # 把繼承者的「值」塞進來
                root.left = self.deleteNode(root.left, now.val) # 再把左邊小樹裡面的舊的node殺掉
            else:
                return 
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root 
