import keyboard

class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        node = self.root
        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True

    def suggestionsword(self, node, word):
        if node.last and keyboard.read_hotkey() == "tab":
            print(word)
        for a, n in node.children.items():
            self.suggestionsword(n, word + a)

    def AutoSuggestions(self, key):
        node = self.root
        for a in key:
            if not node.children.get(a):
                return 0
            node = node.children[a]
        if not node.children:
            return -1
        self.suggestionsword(node, key)
        return 1