class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #Elements present at the edge can contribut at max 1 
                if col*row>0 and matrix[row][col]:
                    #Others can contribute min of top,, left and top left diagonal element as we are moving towards right in a particular row
                    matrix[row][col] += min( matrix[row-1][col], matrix[row-1][col-1], matrix[row][col-1])
                n += matrix[row][col]
        return n
