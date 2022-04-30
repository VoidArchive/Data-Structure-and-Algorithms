'''
Difficulty: Easy
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''

class Solution(object):
    def isPalindrome(self, s):
        """
        Use isalnum to clean the string of space and symbols.

        """
        forward_string = ''.join(char for char in s if char.isalnum()).lower()
        print(forward_string)

        backward_string = forward_string[::-1]

        print(backward_string)
        
        if forward_string == backward_string:
            return True

        return False


