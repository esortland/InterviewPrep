# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.]
# No duplicates!

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while r > l and nums[r] == nums[r-1]:
                        r-= 1
                    l+= 1
                    r-= 1
            
        return res
