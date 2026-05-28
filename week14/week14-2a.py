# week14-2a.py 學習計畫 1D DP 第1題 Easy
# LeetCode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1] + [0] * n
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]
        return a[n]