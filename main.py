from Trie import *

# Trie -------------------------------------------------------------------------
t = Trie()
# File -------------------------------------------------------------------------
fileinput =open("words.txt")

t = Trie()

for word in fileinput.readlines():
    t.insert(word)

user_input = input()
var = t.AutoSuggestions(user_input)

if var == -1:
    print("Trie is Empty...\n")
elif var == 0:
    print("No words found with this title...\n")