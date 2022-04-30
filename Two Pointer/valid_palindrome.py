'''
Difficulty: Easy
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

The best solution is to use pointer with built isalnum() function.

'''


class Solution(object):
    def isPalindrome(self, s):
        """
        Use isalnum to clean the string of space and symbols.
        Reverse the string using [::-1]
        """
        forward_string = ''.join(char for char in s if char.isalnum()).lower()
        backward_string = forward_string[::-1]

        return forward_string == backward_string

    def isPalindrome_with_pointer(self, s):
        """
        Use Pointer to point at the begining and end of the string. Then check if both are same.
        while, skipping all non alpha numberic character.
        Make sure to check if left pointer is not greater or equal to than right pointer.
        """

        left_pointer, right_pointer = 0, len(s) - 1

        while left_pointer < right_pointer:

            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1

            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False


            left_pointer += 1
            right_pointer -= 1

        return True




