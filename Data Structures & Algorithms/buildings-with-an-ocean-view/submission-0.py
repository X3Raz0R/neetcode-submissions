class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        results = []

        for i in range(len(heights) - 1, -1, -1):
            ok = True

            for j in range(i + 1, len(heights)):
                if heights[j] >= heights[i]:
                    ok = False
                    break

            if ok:
                results.append(i)

        results.sort()
        return results