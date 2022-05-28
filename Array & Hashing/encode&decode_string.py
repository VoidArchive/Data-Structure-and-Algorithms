'''
Difficulty: Medium
https://leetcode.com/problems/encode-and-decode-strings/
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode





'''


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s

        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "$":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length

        return res


x = Solution()

y = x.encode(["lint", "code", "love", 'you3$'])

z = x.decode(y)

print(y)
print(z)
