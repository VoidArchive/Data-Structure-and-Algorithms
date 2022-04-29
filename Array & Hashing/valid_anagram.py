'''
Difficulty: Easy

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        Python Cheet Mode:
            Python has a built in Function called counter that does this, 
            Example:
            strl = "aabbaba"
            print(Counter(str1))

            Counter({'a': 4, 'b': 3})
        
        Therefore:

            return Counter(s) == Counter(t) 
            

        OR

        By sorting: if two words are anagram then the sorted value of both strings should be same

        return sorted(s) == sorted(t) 
        

        But the below method is faster
        """
        # To be valid anagram both strings need to have the same length.
        if len(s) != len(t):
            return False

        # Dictionary for counting character one by one
        s_count, t_count = {}, {}

        for i in range(len(s)):
            # The get() method in  dictionary returns:
            # the value for the specified key if key is in dictionary.
            # None if the key is not found and value is not specified.
            # value if the key is not found and value is specified.
            # value is provided

            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for c in s_count:
            if s_count[c] != t_count.get(c, 0):
                return False

        return True

      
