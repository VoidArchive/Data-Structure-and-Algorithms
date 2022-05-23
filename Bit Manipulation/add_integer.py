'''
Difficulty: Medium
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two integers without using the operators + and -.

'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a = a & mask
        while b:
            c = a & b
            a = (a ^ b) & mask
            b = (c << 1) & mask

        # If a is negative in 32 bit sense
        if (a >> 31) & 1:
            return ~(a ^ mask)

        return a


res = Solution()

ans = res.getSum(-1, 1)

print(ans)
