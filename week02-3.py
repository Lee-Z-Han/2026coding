# week02-3.py 學習計畫 Two Pointers 第2題
# LeetCode 392. Is Subsequence
# 一層迴圈, 裡面同時有兩個 index 變數, 叫 two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1,N2 = len(s),len(t) # 字串的長度
        if N1==0: return True # 有陷阱, 如果左邊字串是空的,就不用比了

        i = 0 # 要記得, i從0開始
        for k in range(N2): # 右邊一個個去試
            if s[i] == t[k]: # 找到1個「左右」符合的了
                i += 1 # 左邊的 i 往右升一級
            if i==N1: # 左邊的 i 有走到左邊的結束, 太好了
                return True # 成功
                
        # 沒有走到最後、沒有比對成功, 太糟了
        return False # 失敗