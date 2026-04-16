# week08-5.py 學習計畫 Binary Search 第3題
# LeetCode 162. Find Peak Element 找到「筆左右鄰居大」的那個
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 笨方法: for迴圈不行嗎? (因為老師發現, 這題只有1000個數)
        N = len(nums) # 陣列大小 N
        if N==1: return 0 # i:0 最大 (只有1個數, 就是最大。別再 nums[i-1] nums[i+1]了啦)

        for i in range(N):
            if i == 0: # 沒有左邊, 只測右邊 (要比右邊大)
                if nums[i] > nums[i+1]: return i
            elif i == N-1: # 最右邊、沒有右邊, 只測左邊 (要比左邊大)
                if nums[i] > nums[i-1]: return i
            # 下面會當機, 因為 i-1 或 i+1 可能會超過範圍。所以加上面的 if
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i