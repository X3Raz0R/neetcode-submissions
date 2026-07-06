class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            unu = heapq.heappop(stones)
            doi = heapq.heappop(stones)

            if doi > unu:
                heapq.heappush(stones, unu - doi)

        return -stones[0] if stones else 0