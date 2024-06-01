class Solution:
    # AC, fast and sample
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        overlap = []
        lastResult = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                lastResult[:] = intervals[i:]
                break
            else:
                overlap.append(interval)

        if len(overlap) == 0:
            overlap.append(newInterval)

        return result + [[min(newInterval[0], overlap[0][0]), max(newInterval[1], overlap[-1][1])]] + lastResult
