class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, num in zip(range(len(nums)), nums):
            if num in numDict:
                return [numDict[num], idx]
            else:
                numDict[target - num] = idx
