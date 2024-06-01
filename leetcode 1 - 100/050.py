class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)

        resultDict = {}
        resultDict[0] = 1
        resultDict[1] = x

        def Pow(n):
            if n not in resultDict:
                r = n // 2
                result = Pow(r) * Pow(n - r)
                resultDict[n] = result
                return result
            else:
                return resultDict[n]

        return Pow(n)
