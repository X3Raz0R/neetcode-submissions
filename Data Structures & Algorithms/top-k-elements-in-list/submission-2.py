class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        raspuns = []
        for i,x in count.most_common():
            if k > 0:
                raspuns.append(i)
            k-=1
        return raspuns