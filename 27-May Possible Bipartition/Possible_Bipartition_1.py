class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N==1:
            return True
        if dislikes is None:
            return True
        
        initial_length = len(dislikes)
        gr1 = set()
        gr2 = set()
        
        first = dislikes.pop(0)
        gr1.add(first[0])
        gr2.add(first[1])
        
        #print("Gr1 = ", gr1)
        #print("Gr2 = ", gr2)
        ct = 0
        
        while dislikes:
            curr = dislikes.pop(0)
            if curr[0] not in gr1 and curr[1] not in gr1 and curr[0] not in gr2 and curr[1] not in gr2:                         dislikes.append([curr[0], curr[1]])
            
            elif curr[0] in gr1:
                if curr[1] in gr1:
                    return False
                gr2.add(curr[1])
                #print("gr1 = ", gr1, " gr2 = ", gr2)

            elif curr[0] in gr2:
                if curr[1] in gr2:
                    return False
                gr1.add(curr[1])
                #print("gr1 = ", gr1, " gr2 = ", gr2)
                
            elif curr[1] in gr1:
                if curr[0] in gr1:
                    return False
                gr2.add(curr[0])
                #print("gr1 = ", gr1, " gr2 = ", gr2)
            
            elif curr[1] in gr2:
                if curr[0] in gr2:
                    return False
                gr1.add(curr[0])
                #print("gr1 = ", gr1, " gr2 = ", gr2)
                
            ct += 1
            if ct==initial_length:
                if len(gr1)==len(gr2)==1:
                    return False
                
        return True
