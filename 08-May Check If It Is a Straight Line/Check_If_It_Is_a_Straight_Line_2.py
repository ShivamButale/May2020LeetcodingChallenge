class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        y1y2 = 0
        x1x2 = 0
        
        if (len(coordinates) == 2): 
            return True;

        ydiff = coordinates[1][1] - coordinates[0][1]
        xdiff = coordinates[1][0] - coordinates[0][0]
                                                                  # (x3-x2)*(y2-y1) == (y3-y2)*(x2-x1)
        for i in range(2, len(coordinates)):
            if (((coordinates[i][0]-coordinates[1][0])*ydiff) != ((coordinates[i][1]-coordinates[1][1])*xdiff)):
                return False;
        return True;
