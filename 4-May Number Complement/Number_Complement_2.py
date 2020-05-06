class Solution:
    def findComplement(self, num: int) -> int:
        #nNbB
        x = bin(num)
        z = str(x[2:])
        print(z)
        z = z.replace('0','a')
        z = z.replace('1','0')
        z = z.replace('a','1')
        print(z)
        q = int(z,2)
        return q
