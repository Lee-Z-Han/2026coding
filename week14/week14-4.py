# week14-4.py 學習計畫 DP - 1D 第2題 Medium 題
# LeetCode 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache # 遇到 DP 的題目, 就用 Top-Down DP 來思考, 特別簡單
        def helper(i): # 如果搶到2第i間房, 最後可以拿到多少錢?
            if i >= len(nums): return 0 # 整條街走完了, 沒得搶了
            return nums[i] + max(helper(i+2), helper(i+3))
            # 函式呼叫函式, 來解 Top-Down DP
        return max(helper(0), helper(1))