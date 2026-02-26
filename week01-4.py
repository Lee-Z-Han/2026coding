# week01-4.py 學習計畫 Array/String 第3題
# LeetCode 1431. Kids With the Greatest Number of Candies
# 你給額外的 extraCandies 後, 小朋友手上的糖果, 會不會是最多的
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = [] # 答案的 True 和 False 將塞在裡面
        best = max(candies) # 目前小朋友「最多有幾個糖」?
        for candie in candies: # 逐一檢查、如果把 extraCandies 給小朋友
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False) # 它會不會 >= 最多的, 依序塞入 ans
        return ans