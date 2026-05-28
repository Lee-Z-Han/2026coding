# week14-2b.py 學習計畫 1D DP 第1題 Easy
# LeetCode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        @cache # 函式呼叫函式 (不要重複問答案)
        def helper(i):
            if i<3: return a[i]
            return helper(i-1) + helper(i-2) + helper(i-3)
        return helper(n)