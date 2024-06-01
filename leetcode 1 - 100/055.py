class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        right = nums[0]

        for i, n in enumerate(nums[:-1]):
            if i <= right:
                right = max(right, i + n)
            else:
                break

        return right >= target
