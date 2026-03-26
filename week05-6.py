# week05-6.py 學習計畫 Hash Table (Map/Set) 第4題
# LeetCode 2352. Equal Row and Column Pairs
# 橫的、直的, 完全相同「有幾組」
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() # Hash Map 可以知道有哪些 row 出現幾次
        for row in grid: # 每個 row 逐一處理
            # tuple() 可以把陣列[3,1,2,2], 變不會動 (3,1,2,2)
            counter[tuple(row)] += 1 # 不會動的, 才能當key放入 Hash Map
        
        ans = 0 # 有幾組?
        for col in zip(*grid): # 矩陣 transpose 再取出 col
            ans += counter[tuple(col)]
        return ans