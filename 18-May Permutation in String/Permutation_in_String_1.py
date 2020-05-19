from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 is None:
            return True
        if s2 is None:
            return False
        
        l_s1 = len(s1)
        
        c1 = Counter(s1)
        c2 =  Counter()
        
        index=0
        for i in range(0, len(s2)):
            c2[s2[i]] += 1
            if i+1 >= l_s1:
                if c1==c2:
                    return True
                
                if c2[s2[index]]>1:
                    c2[s2[index]] -= 1
                else:
                    del c2[s2[index]]
                    
                index+=1
                
        return False
