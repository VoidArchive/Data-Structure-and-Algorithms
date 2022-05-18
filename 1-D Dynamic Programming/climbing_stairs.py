'''
Difficulty: Easy
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



'''


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n-1):

            temp = one
            one = one + two
            two = temp
        return one
