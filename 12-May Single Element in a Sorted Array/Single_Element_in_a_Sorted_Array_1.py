class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if nums is None:
            return None
        s = set(nums)
        for i in s:
            if nums.count(i)==1:
                return i
        return None
