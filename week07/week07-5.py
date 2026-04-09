# week07-5.py 學習計畫 Queue 第1題
# LeetCode 933. Number of Recent Calls 想知道 3000 範圍內, 有幾個ping
class RecentCounter:

    def __init__(self): # 一開始物件的「建構子constructor」只呼叫一次
        # 使用 Queue 的資料結構, 但 Python 有 collections.deque
        # Double End Queue 簡稱 deque() 再 LeetCode 可直接用它
        self.queue = deque() # 宣告一個物件裡用 self 找到的 queue 變數

    def ping(self, t: int) -> int:
        self.queue.append(t) # 從右邊塞入1個數
        while self.queue[0] < t-3000: # (目前最左邊、最古老的t)超過範圍
            self.queue.popleft() # Python 的左邊吐掉
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)