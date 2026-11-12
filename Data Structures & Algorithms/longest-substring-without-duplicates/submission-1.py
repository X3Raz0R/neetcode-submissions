class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setul = set()
        l, r = 0, 0
        numarmax = 0
        while r < len(s):
            if s[r] in setul:
                setul.remove(s[l])      # duplicat: micșorăm din stânga
                l += 1
            else:
                setul.add(s[r])         # nou: extindem la dreapta
                numar = r - l + 1
                if numar > numarmax:
                    numarmax = numar
                r += 1
        return numarmax