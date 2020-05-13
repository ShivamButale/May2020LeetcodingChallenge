class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        k = 0
        for i in J:
            k = k + S.count(i)
        return k;
