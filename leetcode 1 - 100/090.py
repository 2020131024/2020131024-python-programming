class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(cur, idx):
            res.append(cur[:])
            
            prev = -11 # -10 <= nums[i] <= 10
            for i in range(idx, len(nums)):
                if prev == nums[i]:
                    continue
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()
                prev = nums[i]
            
        dfs([], 0)
        return res
