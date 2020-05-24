class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in A:
            for j in B:
                a = max(i[0], j[0])
                b= min(i[1], j[1])
                if b>=a:   
                    ans.append([a,b])
        return ans
