##Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

##Your algorithm's runtime complexity must be in the order of O(log n).

##If the target is not found in the array, return [-1, -1].

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        h = len(nums)-1
        
        while l <= h:
            m = (l + h) // 2
            if nums[m] > target:
                h = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return [self.findLow(m, nums, target), self.findHi(m, nums, target)]
            
        return [-1, -1] 
    
    def findLow(self, l, nums, target):
        while l >= 0:
            if nums[l] == target:
                l-=1
            else:
                return l + 1
        return l+1

    def findHi(self, r, nums, target):
        while r < len(nums):
            if nums[r] == target:
                r+=1
            else:
                return r - 1
        return r - 1
