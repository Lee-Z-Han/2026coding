# week03-2.py 學習計畫 Sliding Window 第1題
# LeetCode 643. Maximum Average Subarray I
# 找到長度k的小陣列(平均最大), 找到total最大即可
# 用 Sliding Window 毛毛蟲的解法 右邊吃、左邊吐, 保持長度是k
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums) # 陣列的長度
        total = sum(nums[:k]) # 加總 [:k] 前k項 (長度k的小陣列)
        maxTotal = total
        for i in range(k,N): # 右邊的頭
            total = total + nums[i] - nums[i-k]
            # nums[i] 右邊的頭(往右吃), nums[i-k]左邊的尾, 吐出來
            maxTotal = max(maxTotal,total) # 持續更新, 找到最大的total
        return maxTotal / k # 最大的平均 = 最大的total / k