# class Trie:

#     def __init__(self):
#         self.word = []
        

#     def insert(self, word: str) -> None:
#         self.word.append(word)
        

#     def search(self, word: str) -> bool:
#         if word in self.word :
#             return True
#         else :
#             return False

#     def startsWith(self, prefix: str) -> bool:
#             length = len(prefix)
#             prefixlist = [word[0 : length] for word in self.word if len(word) >= length]
#             if prefix in prefixlist :
#                 return True
#             else :
#                 return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) :

        cur=self.root

        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]

        cur['*']=''

    def search(self, word: str) :

        cur=self.root
        for letter in word:
            if letter not in cur:
                return False
            cur=cur[letter]

        return '*' in cur
        
    def startsWith(self, prefix: str) :

        cur=self.root
        for letter in prefix:
            if letter not in cur:
                return False
            print(cur)
            cur=cur[letter]

        return True
    
trie = Trie();
trie.insert("apple");
trie.insert("thee");  
trie.insert("tree");   
trie.startsWith("tre");
 