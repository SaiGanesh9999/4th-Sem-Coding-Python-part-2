class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        winsum=sum(Arr[:K])
        maxsum=winsum
        for i in range(N-K):#0<5
            winsum=winsum-Arr[i]+Arr[i+K]
            maxsum=max(maxsum,winsum)
        return maxsum
