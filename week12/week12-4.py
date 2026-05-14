# week12-4.py 學習計畫 Graph - DFS 第3題 Medium 題
# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
# 有 N 個城市, 有 N-1 條路, 希望大家走到 0 都是正向, 但不是正向的, 有幾條路?
# 解法：從 0 出發, 全部走過, 路不對, 就 ans += 1
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set() # 走過的, 不要再走
        path = defaultdict(list) # path[now] 與哪些城市相接
        for a,b in connections:
            path[a].append((b, +1))
            path[b].append((a, -1))

        def helper(now):
            ans = 0 # 有幾條路「方向不對」
            visited.add(now)
            for k,d in path[now]: # 城市 now 可以到城市k, 方向是d
                if k not in visited:
                    if d==+1: ans += 1 # 要檢測方向, 若方向「出錯」+1
                    ans += helper(k) # 函式呼叫函式, 裡面會有幾條「出錯」
            return ans
        return helper(0) # 從 0 出發