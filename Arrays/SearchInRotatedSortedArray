# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        
        while l <= h:
            m = (l + h) //2
            
            if nums[m] == target:
                return m 
            
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[h]:
                    l = m + 1
                else:
                    h = m -1
                    
        return -1
