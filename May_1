import math
class Solution:
    def binary_search(self,left,right):
        while left<right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left=mid+1
        return left
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary_search(1, n)
