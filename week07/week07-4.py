# week07-4.py 學習計畫 Stack 第3題, 有點難
# LeetCode 394. Decode String
# 將字串解碼 「數字」代表「重複的次數」會把右邊「方括號」裡的字串重複
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # 利用 stack 處理「方括號」, 及對應的「數字」
        nowN, nowS = 0, '' # 左邊 nowN 數字 vs. 右邊 nowS 字串
        for c in s:
            if c.isdigit(): # 若是數字 就用十進位組合起來
                nowN = nowN * 10 + int(c)
            elif c.isalpha(): # 如果是字母 就讓「字串」變長
                nowS += c
            elif c=='[': # 上括號：「數字」「字串」放入stack
                stack.append( (nowN, nowS) )
                nowN, nowS = 0, '' # 一組新的「數字」「字串」
            elif c==']': # 下括號：取出「數字」「字串」
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS # 重複的次數 * 字串
        return nowS