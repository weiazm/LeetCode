class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #���ȶ���������O(nlogn),�ڽ���һ�α���O(n),�ܸ��Ӷ�O(nlogn)
        if(k < 0):
            return 0
        else:
            num = 0
            idx = 0
            nums.sort()
            while(idx<len(nums)-1):
                y = idx + 1
                while (y < len(nums)-1 and nums[y] < nums[idx]+abs(k)):
                    y = y+1
                if(nums[y] == nums[idx]+abs(k)):
                    num = num+1
                while(idx < len(nums)-1 and nums[idx] == nums[idx + 1]):
                    idx = idx + 1
                idx = idx + 1
            return num