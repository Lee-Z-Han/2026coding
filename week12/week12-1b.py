# week12-1b.py 學習計畫 Graph - DFS 第1題 Medium 題
# LeetCode 841. Keys and Rooms
# 房間裡有鑰匙, 可以再開新的房間。最後能開全部房間嗎?
# DFS: Depth First Search 通常會利用 stack 或 function stack (函式呼叫函式)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def helper(now): # 函式呼叫函式的版本, 也能進行 DFS
            for k in rooms[now]:
                if k not in visited:
                    visited.add(k)
                    helper(k)
        visited.add(0)
        helper(0)
        return len(rooms) == len(visited)