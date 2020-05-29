class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[]
        for i in range(0, num+1):
            res.append(bin(i).count('1'))
        return res
