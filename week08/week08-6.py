# week08-6.py 學習計畫 Binary Search 第4題
# LeetCode 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 準備一個函式 helper(ans) 看答案對不對
        def helper(k): # 1小時吃k個香蕉, 能成功h小時吃完嗎?
            total = 0 # 你猜k, 它會用多少時間
            for pile in piles: # 很多堆香蕉, 逐一檢查
                total += pile // k # 要吃掉這堆香蕉 pile 要花多少時間
                if pile % k > 0: total += 1 # 有餘數, 再多1小時
            return total <= h # 符合條件(在h小時內吃完)
        return bisect_left( range(1,max(piles)), True, key=helper) + 1