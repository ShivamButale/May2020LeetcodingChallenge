class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        #Tried solving by maintaing 2 ptrs. Results in wrong answers for some cases.so let us go for DP and maintain a 2d matrix which maintains counts
        matrix = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                #If both lie in 1 straight line
                if(A[i - 1] == B[j - 1]):
                    matrix[i][j] = 1 + matrix[i - 1][j - 1]
                else:
                    #chooose max count
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        return matrix[len(A)][len(B)]
        
