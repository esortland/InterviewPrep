# Given a collection of distinct integers, return all possible permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[1+i:], path + [nums[i]], res)
