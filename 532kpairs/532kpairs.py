class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #用同长度的两个list表示当前值的左右两个k-pairs是否取到，同时维护pair中两个数的flag表
        num = 0;
        rflag = [0]*len(nums)
        lflag = [0]*len(nums)
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                if(nums[y] - nums[x] == k):
                    if(rflag[x] == 0 and lflag[y] == 0):
                        rflag[x] = 1
                        lflag[y] = 1
                        num = num+1
                    else:
                        rflag[x] = 1
                        lflag[y] = 1
                if(nums[y] - nums[x] == -k):
                    if(lflag[x] == 0 and rflag[y] == 0):
                        lflag[x] = 1
                        rflag[y] = 1
                        num = num+1
                    else:
                        lflag[x] = 1
                        rflag[y] = 1
        if (k == 0):
            return (int)(num/2)
        elif (k < 0):
            return 0
        else:
            return num