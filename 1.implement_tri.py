# Leetcode: 208 (implement trie)

# Build tri and chech if (i)any word exist or not (ii)any word start with given word or not

class TriNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie():
    def __init__(self) -> None:
        self.root = TriNode()
    
    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.word

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
