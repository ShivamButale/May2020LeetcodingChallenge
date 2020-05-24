class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        x = []
        i = j = 0

        while i < len(A) and j < len(B):            
            low = max(A[i][0], B[j][0])         #picks lower edge of intersection
            high = min(A[i][1], B[j][1])        #picks upper edge of intersection
            if low <= high:
                x.append([low, high])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return x
