class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for a in range(len(s)):
            countS[s[a]] = 1 + countS.get(s[a], 0)
            countT[t[a]] = 1 + countT.get(t[a], 0)
            
        return countS == countT