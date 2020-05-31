class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dict1 = defaultdict(list)
        for i in points:
            dist = math.sqrt(i[0]**2 +  i[1]**2)
            dict1[dist].append(i)
        cc = sorted(dict1.items(), key=lambda x:x[0])
        ct =0
        ans = []
        for i in range(0, len(cc)):
            for j in range(0, len(cc[i][1])):
                if ct==K:
                    return ans
                else:
                    ans.append(cc[i][1][j])
                    ct+=1
        return ans
