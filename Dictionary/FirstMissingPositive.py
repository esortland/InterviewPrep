# Given an unsorted integer array, find the smallest missing positive integer.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if i > 0:
                dic[i] = 1
        
        j = 1 
        while True:
            if j in dic:
                j += 1
            else:
                return j
