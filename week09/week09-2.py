# week09-2.py 學習計畫 Linked List 第3題 Easy 題
# LeetCode 206. Reverse Linked List
# 把它反過來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] # 容易理解的方法, 把 linked list 變成陣列
        while head: # 只要還有資料
            a.append(head.val) # 就塞到陣列 a 的後面
            head = head.next # 換下一筆
        # print(a) 印出來, 成功變成我們習慣的摁列 a[i]
        now = ans = ListNode() # 答案將串到裡面

        # 下面用倒過來的迴圈, 把陣列的值, 逐一串到 ans 的後面
        N = len(a) # 陣列的長度, 要倒過來的迴圈
        for i in range(N-1, -1, -1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next