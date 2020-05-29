class Solution:
    def countBits(self, num: int) -> List[int]:
        li = []
        for i in range(num+1):
#            x = str(bin(i))
#            w = x.count('1')
#            li.append(w)
            li.append(str(bin(i)).count('1'))
        return li
