class Trie:

    #Trie data struture maintains words according to their start symbol.We go for dictionary implementation
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.dict
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr["#"]=True           #End of word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.dict
        for i in word:
            if i not in curr:
                return False
            curr = curr[i]
        
        if '#' not in curr:
            return False #Word continues further, hasnt ended yet
        return True #Word has occured

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.dict
        for i in prefix:
            if i not in curr:
                return False
            curr = curr[i]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
