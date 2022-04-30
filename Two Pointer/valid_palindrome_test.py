import unittest
from valid_palindrome import Solution


class TestPalindrome(unittest.TestCase):

    def test_isPalindrome(self):

        self.assertTrue(Solution.isPalindrome(self,"A man, a plan, a canal: Panama"))
        self.assertTrue(Solution.isPalindrome(self," "))

        self.assertFalse(Solution.isPalindrome(self,"race a car"))



if __name__=="__main__":
    unittest.main()