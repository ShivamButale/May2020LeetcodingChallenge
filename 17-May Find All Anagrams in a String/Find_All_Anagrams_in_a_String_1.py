from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Taking slices of lenght p from s and comapring the counts, exceeds the time limit. Already tried that. So lets try to build a dynamic counter for s 
        
        
        if s is None:
            return None
        if p is None:
            return None
        
        pp = len(p) 
        xx = Counter(p)
        ss = Counter()
        l = []
        
        index = 0
        for i in range(0, len(s)):
            ss[s[i]] += 1
            if i+1 >= pp:
                if ss == xx:
                    l.append(index)            
            
                #Shift  to right,so decrease count of index i.e first element by  1
                if ss[s[index]]>1:
                    ss[s[index]] -= 1
                else:
                    del ss[s[index]]
                
                index+=1 #Shift right by 1 unit
    
        return l
