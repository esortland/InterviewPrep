# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.getCommon(prefix, strs[i])
        return prefix

    def getCommon(self, prev, cur):
        shorter =  cur if len(prev) > len(cur) else prev
        longer = cur if shorter == prev else prev
            
        for i in range(len(shorter)):
            if shorter[i] != longer[i]:
                return shorter[:i]
        
        return shorter
