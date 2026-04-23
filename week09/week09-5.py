# week09-5.py 學習計畫 Linked List 第1題 Medium 題 有點難 把中間的node刪掉
# LeetCode 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None # 很討厭的機車的狀況: 只有1個, 避不掉

        prev = fast = slow = head # fast兔子 slow烏龜 一開始都在最前面

        while fast != None and fast.next != None: # 兔子還沒到終點
            fast = fast.next.next # 兔子跳2格
            prev = slow # 烏龜在走之前, 先記下前一格的位置
            slow = slow.next # 烏龜走1格
        # print(slow.val) # 當兔子到終點時, 烏龜在中間(沒錯)
        prev.next = slow.next
        return head