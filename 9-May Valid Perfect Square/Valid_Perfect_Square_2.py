class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1 or num == 4or num == 9:
            return True
        for i in range(2,int(num/4+1)):
            if (i*i) == num:
                return True
        return False
