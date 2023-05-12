class Solution:
    def pivotIndex(self, nums):
        n=len(nums)
        rsum=sum(nums)
        lsum=0
        for i in range(0,n):
            rsum=rsum-nums[i]
            if lsum==rsum:
                return i
            lsum=lsum+nums[i]
        return -1
