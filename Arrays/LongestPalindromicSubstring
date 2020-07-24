# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# First Try, works on small input but is much too slow:
# It goes through all possible substrings which is very very inefficient.

def isPalindrome(s): 
    for i in range(len(s)-1):
        r = len(s) - 1 - i
        if s[i] != s[r]:
            return False 
    return True
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        max_str = ''
        max_len = 0
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                subString = s[i:j]
                subLen = len(subString)
                if isPalindrome(subString) and subLen > max_len:
                    max_str = subString
                    max_len = subLen
        return max_str


# Second try, works and is faster:
# While trying to get a substring it only grabs as much that is a palindrome,
# previously I was finding a substring then checking. This is much better

def getPalindrome(s, l, r): 
    while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            res = max(getPalindrome(s, i, i), getPalindrome(s, i, i+1), res, key=len)
            
        return res
