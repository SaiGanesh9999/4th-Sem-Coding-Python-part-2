from itertools import permutations
class Solution:
    def find_permutation(self, S):
        p=permutations(S)
        m=[''.join(list(i)) for i in p]
        l=[]
        for i in m:
            if i not in l:
                l.append(i)
        return sorted(l)
