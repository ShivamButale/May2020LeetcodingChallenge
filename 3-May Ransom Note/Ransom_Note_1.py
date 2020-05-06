class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote is None:
            return True
        if magazine is None:
            return False
        s1 = set(ransomNote)
        for i in s1:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
