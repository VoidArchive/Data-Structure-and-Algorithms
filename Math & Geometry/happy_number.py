class Solution:
    def isHappy(self, n: int) -> bool:

        slow, fast = n, self.sumSquare(n)

        while slow != fast:
            fast = self.sumSquare(fast)
            fast = self.sumSquare(fast)
            slow = self.sumSquare(slow)

        return True if fast == 1 else False

    def sumSquare(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10

        return output


s = Solution()
print(s.isHappy(20))
