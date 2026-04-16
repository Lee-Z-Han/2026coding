# week08-2.py 學習計畫 Binary Search 第1題
# LeetCode 374. Guess Number Higher or Lower
# 給你 guess() 你可以呼叫它, 找出 1...n 裡面的「答案」

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 方法1: 神奇的 bisect_left() 寫法, 只要1行
        # for i in range(n+1): print( -guess(i), end=' ') # 做個實驗, 不用寫
        return bisect_left( range(n+1), 0, key=lambda x:-guess(x) ) # 一行抵下面7行
        # for i in range(1, n+1): # 「錯誤」的暴力法, for迴圈找答案
        #     if guess(i) == 0: return i # 猜中了, 答案是i
        # 不能用上面的 for迴圈, 因為 n 有 20億這麼大, 試不完
        # 要用小學「猜數字」每次範圍猜一半, 比它大, 比它小, 縮小範圍
        # 方法2: while left < right: 去逼近
        left, right = 1, n+1 # 左右的範圍 (左「包含」、右「不包含」)
        while left < right: # 左右的範圍還沒「撞在一起」
            mid = (left + right) // 2 # (猜)中間的數
            if guess(mid) == 0: return mid # 猜到中間的數字
            if guess(mid) > 0: left = mid + 1 # (暗示你) 再高一點 (中點設成下界)
            else: right = mid # (暗示你) 再低點 (中點設成上界)
        return left
        # week08-3 是要寫在紙上, 把這題 Easy 題的 left, right, mid 跟猜的數字搞懂