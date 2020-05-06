class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                z = magazine.find(i)
                if z == -1:
                    return False
                magazine = magazine.replace(i,'',1)
                #print(magazine)
            else:
                return False
        return True
