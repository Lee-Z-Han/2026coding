# week12-5.py 學習計畫 Graph - DFS 第4題 Medium 題
# LeetCode 399. Evaluate Division
# 有很多分子、分母 的除法關係
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(list)
        for (a,b),v in zip(equations,values): # 用拉鍊壓縮起來
            path[a].append((b, v)) # 正的走
            path[b].append((a, 1/v)) # 倒著走
        def helper(now, target, v0):
            if now not in path or target not in path: return -1 # 有異物出現, 不要算了
            if now == target: return v0
            visited.add(now)
            ans = -1
            for node, v in path[now]:
                if node not in visited: # 沒走過, 就可走走看、試看看
                    ans = max(ans, helper(node, target, v0*v) )
            return ans
        ans = []
        for a,b in queries:
            visited = set()
            ans.append( helper(a, b, 1) )
        return ans