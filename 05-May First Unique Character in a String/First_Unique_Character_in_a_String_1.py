class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None:
            return -1
        for i in range(0, len(s)):
            if s.count(s[i])==1:
                return i
        return -1
