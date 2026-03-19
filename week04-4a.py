# week04-4a.py (重寫 week04-2.py)
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度 (一百加, 就好了!!!)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 # 一開始的高度是 0
        for gg in gain: # Python 的進階 for 迴圈寫法, 依次取出 gg
            H += gg
            ans = max(ans,H)
        return ans

# week04-2.py 學習計畫 prefix sum 第1題
        N = len(gain) # 陣列的長度 N
        ans = H = 0 # 一開始的高度是 0
        # 答案一開始是0, 因為一開始的高度是0
        for i in range(N): # 逐個加起來
            H += gain[i] # 現在增減的量 gain[i] 加進 H
            ans = max(ans,H) # 更新最高的答案
        return ans