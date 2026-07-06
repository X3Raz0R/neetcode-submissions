class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        if len(intervals)==1:
            return intervals
        for i in range(1, len(intervals)):
            i1s = intervals[i-1][0]
            i2e = intervals[i-1][1]
            j1s = intervals[i][0]
            j2e = intervals[i][1]

            if i2e >= j1s:
                # actualizează intervalul curent
                intervals[i] = [i1s, max(i2e, j2e)]
            else:
                # intervalul precedent este final
                res.append([i1s, i2e])

            if i == len(intervals) - 1:
                res.append(intervals[i])

        return res