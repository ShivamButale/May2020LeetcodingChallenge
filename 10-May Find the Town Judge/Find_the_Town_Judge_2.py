class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        if(len(trust)) == 1:
            return trust[0][1]
        m = list(range(1, N+1))                 #possible judges
        k = list(range(1, N+1))
        for [x,y] in trust:
            if x in m:
                m.remove(x)
            if y in k:
                k.remove(y)
       
        if not m:
            return -1                          #everyone trusts someone
    
        for i in m:
            for j in k:
                if [j,i] not in trust:
                    #print([j,i])
                    return -1
            return i
                
            
