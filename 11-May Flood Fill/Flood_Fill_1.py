class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        init  = image[sr][sc]
        
        def helper(i, j, newColor, init):
            if (i<0 or i>=rows or j<0 or j>=cols or image[i][j]!=init or image[i][j]==newColor):
                return 
            image[i][j] =  newColor

            helper(i+1, j, newColor, init)
            helper(i-1, j, newColor, init)
            helper(i, j+1, newColor, init)
            helper(i, j-1, newColor, init)

        helper(sr,sc,newColor, init)
        return image
