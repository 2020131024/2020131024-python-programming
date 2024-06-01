# AC, fast
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda val: val[0])
        
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
