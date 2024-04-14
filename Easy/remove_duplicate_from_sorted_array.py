class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in range(1, len(nums)):
            # if i <= len(nums)-2:
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
                    # del nums[i+1]
        return k

            