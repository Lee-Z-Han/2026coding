# week05-4.py 昨天 2025-03-25的挑戰題
# LeetCode 3546. Equal Sum Grid Partition I
# grid 矩陣, 能否「切一刀」兩邊和「剛好相同」
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid]) # 全部加起來

        preSum = 0 # 對應「橫切一刀」
        for row in grid: # 逐個 row 處理
            preSum += sum(row) # 把row整行加進來
            if preSum == total - preSum: # 上半部 == 下半部
                return True

        preSum = 0 # 對應「直切一刀」
        for col in zip(*grid): # 把 transpose 轉置矩陣, 逐個處理
            preSum += sum(col)
            if preSum == total - preSum: # 左半部 == 右半部
                return True

        return False