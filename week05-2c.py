# week05-2c.py 學習計畫 Hash Table (Map/Set) 再寫第三個版本, 善用 set()
# LeetCode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2) # (第二個版本)
        return [list(nums1 - nums2), list(nums2 - nums1)] # 第三個版本