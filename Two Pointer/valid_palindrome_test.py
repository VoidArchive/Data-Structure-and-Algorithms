import unittest
from valid_palindrome import Solution


class TestPalindrome(unittest.TestCase):

    def test_isPalindrome(self):

        self.assertTrue(Solution.isPalindrome(self,"A man, a plan, a canal: Panama"))
        self.assertTrue(Solution.isPalindrome(self," "))

        self.assertFalse(Solution.isPalindrome(self,"race a car"))



    def test_isPalindrome_with_pointer(self):

        self.assertTrue(Solution.isPalindrome_with_pointer(self,"A man, a plan, a canal: Panama"))
        self.assertTrue(Solution.isPalindrome_with_pointer(self," "))
        self.assertTrue(Solution.isPalindrome_with_pointer(self,".,"))


        self.assertFalse(Solution.isPalindrome_with_pointer(self,"race a car"))



if __name__=="__main__":
    unittest.main()