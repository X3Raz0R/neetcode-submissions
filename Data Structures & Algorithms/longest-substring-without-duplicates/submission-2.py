class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setul = set()
        l,r =0,0
        numarmax=0
        while r<len(s):
            if s[r] in setul:
                setul.remove(s[l])
                l+=1
            else:
                setul.add(s[r])
                r+=1
                numar = r-l
                if numar > numarmax:
                    numarmax=numar
            
        return numarmax