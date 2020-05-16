class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curr_max=0
        curr_min = 0
        sum = 0
        max_so_far = float("-inf")
        min_so_far = float("inf")
        for i in A:
            sum +=  i
            curr_max = max(0, curr_max)+i
            max_so_far =  max(max_so_far, curr_max)
            
            curr_min = min(0, curr_min)+i
            min_so_far = min(min_so_far, curr_min)
            
        if sum == min_so_far:
            return max_so_far
        
        return max(max_so_far, sum-min_so_far)
