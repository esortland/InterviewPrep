## Get all string permutations with no repeats

def permutations(string):
    res = {}
    dfPerm(string, 0, len(string)-1, res)
    return [x for x in res]

def dfPerm(string, l, r, res):
    if l == r:
        res[string] = 1
    else:
        for i in range(l, r+1):
            string = swap(string, l, i)
            dfPerm(string, l+1, r, res)
            string = swap(string, l, i)
            
def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
