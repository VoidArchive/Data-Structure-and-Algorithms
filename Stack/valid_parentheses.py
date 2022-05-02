'''
Difficulty: Easy

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


'''


class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in p:

                if stack and stack[-1] == p[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False

test = Solution()
print(test.isValid('(())'))