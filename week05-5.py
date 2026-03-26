# week05-5.py 學習計畫 Hash Table (Map/Set)
# LeetCode 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1) # 統計用過的字母、出現的次數
        counter2 = Counter(word2) 
        # 用過的字母, 是否是相同的集合(左邊有、右邊也會有。右邊有、左邊也會有)
        if set(counter1.keys()) != set(counter2.keys()): # 用的字母不同, 就失敗
            return False 
        # 把出現的次數, 小到大排好。如果兩邊都一樣, 那就可以換到一樣為止
        if sorted(counter1.values()) != sorted(counter2.values()): # 次數不同
            return False
        return True