class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0, 1, 2]
        resultLen = len(result)

        for i in range(resultLen, n + 1):
            result.append(result[i-2] + result[i-1])
        
        return result[n]
