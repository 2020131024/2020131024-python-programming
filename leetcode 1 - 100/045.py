class Solution:
    def jump(self, nums: List[int]) -> int:
        maxDist = 0
        end = 0
        jump = 0
        for i in range(len(nums) - 1):
            maxDist = max(maxDist, i + nums[i])
            if i == end:
                end = maxDist
                jump += 1
        return jump
