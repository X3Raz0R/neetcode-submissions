class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        max = 0
        while p1 < p2:
            temp = self.nrmin(height[p1],height[p2]) * (p2-p1) 
            if(temp > max):
                max = temp
            if height[p1] > height[p2]:
                p2 = p2-1
            else:
                p1 = p1 + 1
        return max

        
    def nrmin(self,p1,p2):
        if p1 > p2:
            return p2
        else:
            return p1
        