class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  
        res = r            
        while l <= r:
            k = (l + r) // 2      # mijlocul intervalului
            ore = sum(math.ceil(p / k) for p in piles)

            if ore <= h:         
                res = k
                r = k - 1
            else:                 # k prea mic -> trebuie mai mare
                l = k + 1

        return res