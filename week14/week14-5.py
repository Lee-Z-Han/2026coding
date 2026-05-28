# week14-5.py 學習計畫 DP - 1D 第4題
# LeetCode 790. Domino and Tromino Tiling
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        @cache 
        def helper(n):
            if n==0: return 1
            if n==1: return 1
            if n==2: return 2
            ans = helper(n-1) + helper(n-2)
            # 新的一堆L型
            for i in range(3,n+1):
                ans = (ans + helper(n-i) * 2) % MOD
            return ans 
        return helper(n)