class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l1=[]
        l2=[]
        for i in trust:
            l1.append(i[0])
            l2.append(i[1])
        print("l1 = ", l1, " l2 = ", l2)
        for i in range(1,N+1):
            if l2.count(i) == N-1:
                if i not in l1:
                    return i
        return -1
