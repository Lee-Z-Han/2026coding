# week12-3.py 學習計畫 Graph - DFS 第2題 Medium 題
# LeetCode 547. Number of Provinces 想知道「幾群」是相連的
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected) # 先知道有幾個 Nodes
        visited = set() # 走過的地方, 不要再走

        def helper(now): # 函式呼叫函式, 因為 function stack 就是一種 DFS
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)
        ans = 0 # 有「幾群」是相連的
        for i in range(N): # 全部 node 巡一次
            if i not in visited: # 沒有去過的話
                ans += 1 # 代表是新的一群
                helper(i) # 函式呼叫函式, 暴力把它的鄰居、鄰居的鄰居、...全部走過
        return ans   