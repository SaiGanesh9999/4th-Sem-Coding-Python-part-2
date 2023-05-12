class Solution:
    def equilibriumPoint(self,A, N):
        rs=sum(A)
        ls=0
        for i in range(0,N):
            rs=rs-A[i]
            if ls==rs:
                return i+1
            ls=ls+A[i]
        return -1
