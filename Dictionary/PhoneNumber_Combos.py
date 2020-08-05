class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        pn = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        res = []
        self.dfs(digits, pn, 0, '', res)
        
        return res
        
    def dfs(self, digits, pn, index, combo, res):
        if len(combo) == len(digits):
            res.append(combo)
            return
        for i in range(index, len(digits)):
            for j in pn[digits[i]]:
                self.dfs(digits, pn, i + 1, combo + j, res)
