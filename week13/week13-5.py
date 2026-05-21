# week13-5.py 學習計畫 Heap / Priority Queue 第3題
# LeetCode 2542. Maximum Subsequence Score
# 挑 k 個 index, 讓 nums1 對應的 k 個數相加, 再乘 min(nums2對應k個數) 希望最大
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 先把 nums1 跟 nums2 合併起來
        # ex. [1,3,3,2]
        #     [2,1,3,4]
        N = len(nums1) # 陣列的長度
        a = [ (nums2[i],nums1[i]) for i in range(N)] # 左右合併起來
        # print(a)
        # a.sort() # 小到大排好
        # print(a)
        a.sort(reverse=True) # 大到小排好
        
        heap = [a[i][1] for i in range(k)] # 找到最前面的 k 組數字, 加入 heap 資料結構
        heapify(heap) # 之後將小到大依序吐掉 nums1 的這k個數, 換加入新的n1,n2組
        total = sum(heap)
        ans = total * a[k-1][0] # 前k項的nums1 及對應最小的 nums2 相乘

        for i in range(k,len(nums2)): # 後面將加入的數
            n2,n1 = a[i] # 將加入的對應的數
            heappush(heap, n1) # 加1
            total += n1 - heappop(heap) # 加1；吐1
            ans = max(ans, total*n2) # 更新答案
        return ans