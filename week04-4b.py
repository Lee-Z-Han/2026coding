# week04-4b.py (重寫 week04-3.py)
# LeetCode 3866. First Unique Even Element
# 找到陣列 nums 裡「只出現過1次的偶數」第1次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] * 200
        for nn in nums: # 把陣列的值, 逐一取出來
            H[nn] += 1 # 統計數量
        for nn in nums: # 再來一次, 逐一取出來
            if nn % 2 == 0 and H[nn] == 1: return nn # 偶數 and 落單
        return -1
# week04-3.py More Challenges 的簡單題
        N = len(nums) # 有 N 個數
        # 第1種寫法, 用陣列, 先統計出現的次數
        H = [0] * 200 # 很多很多格, H[??] 對應 ?? 出現幾次
        for i in range(N): # 第一次處理
            H[ nums[i] ] += 1 # 把出現的數字, 塞進 H[??] 裡
        # 再逐個檢查「偶數」出現幾次
        for i in range(N): # 逐一檢查
            if nums[i] % 2 == 0 and H[ nums[i] ] == 1: # 偶數, 只出現一次
                return nums[i] # 找到答案了
        return -1