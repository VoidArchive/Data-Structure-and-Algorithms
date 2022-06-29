'''
Difficulty: Medium

https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


'''


class TrieNode:
    def __init__(self) -> None:
        self.childern = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.childern:
                cur.childern[c] = TrieNode()

            cur = cur.childern[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.childern.values():
                        if dfs(i + 1, child):
                            return True

                    return False

                else:
                    if c not in cur.childern:
                        return False
                    cur = cur.childern[c]

            return cur.word

        return dfs(0, self.root)
