# week05-2b.py 學習計畫 Hash Table (Map/Set) 再寫第二個版本
# LeetCode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2) # 只加這行(第二個版本)
        ans1 = [] # 放「在nums1 但不在 nums2」的數
        for num in nums1: # 逐一取出
            if num not in nums2: # 沒在裡面
                ans1.append(num) # 放入答案
        ans2 = [] # 放「在nums2 但不在 nums1」的數
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(set(ans1)), list(set(ans2))] # 先寫「最爛」的版本
        # 把方括號list變set, 再變回list, 重複的就不見了