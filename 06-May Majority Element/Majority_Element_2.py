class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = []
        x = (len(nums)/2)
        for i in nums:
            if i not in l:
                l.append(i)
                if nums.count(i) > x:
                    return i
