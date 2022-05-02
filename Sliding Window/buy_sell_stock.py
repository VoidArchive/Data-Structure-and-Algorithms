'''
Difficulty: Easy
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left_pointer, right_pointer = 0, 1 
        max_profit = 0

        while right_pointer < len(prices):

            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                max_profit = max(max_profit, profit)
            else:
                left_pointer = right_pointer
        
            right_pointer += 1
            
        return max_profit