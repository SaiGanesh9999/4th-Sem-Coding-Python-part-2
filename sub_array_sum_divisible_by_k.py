class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        summ = 0
        res = 0
        dic = {0:1}
        for a in A:
            summ = (summ + a) % K
            if summ in dic:
                res += dic[summ]
                dic[summ] += 1
            else:
                dic[summ] = 1
        return res
