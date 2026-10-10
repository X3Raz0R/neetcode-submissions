class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l < r:
            while self.numeric(s[l]) == False and l < r:
                l+=1
            while self.numeric(s[r]) == False and l < r:
                r-=1
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else: return False
        return True
           
    
    def numeric(self,a)->bool:
        if a >= "a" and a <= "z":
            return True
        if a >= "A" and a <= "Z":
            return True
        if a >= "0" and a <= "9":
            return True
        else: return False