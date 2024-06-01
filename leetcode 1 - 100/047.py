class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set([()])
        for n in nums:
            thisSet = set()
            for last in result:
                lastList = list(last)
                for i in range(len(last)+1):
                    thisSet.add(tuple(lastList[:i] + [n] + lastList[i:]))
            result = thisSet

        return list(result)
