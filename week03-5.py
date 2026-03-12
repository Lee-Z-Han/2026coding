# week03-5.py 學習計畫 Sliding Window 第4題
# LeetCode 1493. Longest Subarray of 1's After Deleting One Element
# 陣列裡, 一定要刪掉1個, 問剩下的陣列裡, 最長的1有幾個?
# Sliding Window 伸縮自如的蛇蛇, 肚子裡, 可容忍最多1個0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums) # 陣列的長度
        zeros = 0 # 蛇蛇的體內, 有幾個「有毒的0」
        tail = 0 # 蛇蛇的尾巴, 一開始停在 0 的地方, 拉肚子時, 會往右縮
        ans = 0 # 蛇蛇的最長的長度
        for head in range(N): # 蛇蛇的頭頭, 逐一往右吃
            if nums[head] == 0: zeros += 1 # 如果吃到「有毒的0」zeros加1
            while zeros > 1: # 「有毒的0」太多了
                if nums[tail] == 0: zeros -= 1 # 如果拉肚子、拉出「有毒的0」zeros減1
                tail += 1 # 尾巴吐之後, 右縮
            ans = max(ans, head - tail + 1) # 更新蛇蛇的最大長度
        return ans -1 # 題目說, 一定要刪掉1個