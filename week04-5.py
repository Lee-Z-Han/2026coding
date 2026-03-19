# week04-5.py 學習計畫 prefix sum 第2題
# LeetCode 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums) # 陣列的長度

        prefix = [0] # 一開始 prefix sum 只有1個[0]
        for i in range(N):
            prefix.append( prefix[-1] + nums[i] ) # 陣列變長了
        #print(prefix) # debug 印出來看一下

        postfix = [0] * (N+1)
        for i in range(N-1, -1, -1): # 倒過來的迴圈
            postfix[i] = postfix[i+1] + nums[i]
        #print(postfix)

        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        return -1