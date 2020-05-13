class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        
        if n==2:
            return True
        flag=0
        init_num = (coordinates[1][1]-coordinates[0][1])
        init_deno = (coordinates[1][0]-coordinates[0][0])
        
        if init_deno==0:
            flag==1
            init_m = 2**31-1
        else:
            init_m =  init_num/init_deno  
        
        for i in range(1, len(coordinates)-1):
            denominator = (coordinates[i+1][0]-coordinates[i][0])
            numerator = (coordinates[i+1][1]-coordinates[i][1])
            
            if denominator==0:
                if flag==1:
                    continue
                else:
                    return False
                
            m =  numerator / denominator 
            if m !=  init_m:
                return False
            
        return True
