# week14-3a.py 學習計畫 DP - 1D 第2題 Easy 題
# LeetCode 746. Min Cost Climbing Stairs
# 踩在每格的梯上, 都要付出 cost[i] 的代價, 每次可跨1格 or 2格
from functools import * # 在比賽時, 要自己加這行, 才能用 @cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache # 函式呼叫函式, 把大問題, 拆成小問題
        def helper(i): # 現在踩在第i格, 之後要多少錢?
            if i >= len(cost): return 0 # 終止條件
            return cost[i] + min( helper(i+1), helper(i+2) )
        return min( helper(0), helper(1) )