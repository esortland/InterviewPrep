## Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        i = 0 
        romanDic ={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        while i < len(s):
            sym = s[i]
            
            if sym == 'I':
                if i < len(s) -1 and s[i+1] == 'V':
                    val += 4 
                    i += 2
                elif i < len(s) -1 and s[i+1] =='X':
                    val += 9
                    i += 2
                else:
                    val += romanDic[sym]
                    i += 1
            
            elif sym == 'X':
                if i <len(s) -1 and s[i+1] =='L':
                    val += 40 
                    i += 2
                elif i < len(s)-1 and s[i+1] =='C':
                    val += 90 
                    i += 2
                else:
                    val += romanDic[sym]
                    i += 1
            
            elif sym == 'C':
                if i < len(s) -1 and s[i+1] == 'D':
                    val += 400 
                    i += 2
                elif i < len(s) -1 and s[i+1] == 'M':
                    val += 900
                    i += 2
                else:
                    val += romanDic[sym]
                    i += 1
            else:
                    val += romanDic[sym]
                    i += 1
        
        return val
