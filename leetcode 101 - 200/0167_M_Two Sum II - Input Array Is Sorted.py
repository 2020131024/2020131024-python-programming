class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}
        idx = 0
        for num in numbers:
            if num not in numDict:
                numDict[target-num] = idx
            else:
                return [numDict[num] + 1, idx + 1]
            idx += 1
