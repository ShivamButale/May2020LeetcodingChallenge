class Solution:
    def findMaxLength(self, nums):
        dict1 = {}
        maxarr = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count += -1
            if count == 0:
                maxarr = i + 1
            if count in dict1:
                maxarr = max(maxarr, i-dict1[count])
            else:
                dict1[count] = i
        return maxarr
