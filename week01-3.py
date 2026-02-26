# week01-3.py 學習計畫 Array/String 第2題
# LeetCode 1071. Greatest Common Divisor of Strings
# 最大公因數gcd 的字串
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 跟長度的最大公因數gcd有關
        N1, N2 = len(str1), len(str2) # 兩個字串長度
        N = gcd(N1, N2) # 最大公因數
        ans = str1[:N] # 字串1的前面N個字母
        
        if ans*(N1//N) != str1: return "" # 不符合, 就失敗
        if ans*(N2//N) != str2: return ""
        return ans