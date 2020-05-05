class Solution:
    def findComplement(self, num: int) -> int:
        dict1 = {'1':'0','0':'1'}
        x = bin(num)
        x=list(x[2:])
        for i in range(0, len(x)):
            x[i] = dict1[x[i]]
        x = "".join(x)
        s = int(x, 2)
        return s
