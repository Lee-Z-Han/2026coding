# week05-3.py 學習計畫 Hash Table (Map/Set)
# LeetCode 1207. Unique Number of Occurrences
# 每種數字, 出現的「次數」必須「都不一樣」哦!
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) # 統計數字出現的次數
        s = set() # 用來看「出現的次數」是否獨一無二
        for c in counter: # 將數字逐一印出來
            # 測試一下
            #print(c, counter[c]) # 數字、出現幾次(真的有統計好!)
            # 問 counter[c] 是否都獨一無二
            if counter[c] in s: # 如果有出現過, 失敗
                return False
            s.add(counter[c]) # 現在這個出現的次數, 放入 s 裡
        return True # 隨便 return 值