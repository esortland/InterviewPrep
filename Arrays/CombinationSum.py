# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:
 #   All numbers (including target) will be positive integers.
 #   The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.getCombs(candidates, target, 0, [], res)
        return res
        
    def getCombs(self, candidates, target, index, current, res):
        if target < 0:
            return 
            
        if target == 0:
            res.append(current)
        
        for i in range(index, len(candidates)):
            self.getCombs(candidates, target-candidates[i], i, current + [candidates[i]], res)
            
