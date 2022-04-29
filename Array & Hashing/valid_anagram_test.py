import unittest
from valid_anagram import Solution


class TestAnagram(unittest.TestCase):

    def test_isAnagram(self):
        self.assertTrue(Solution.isAnagram(self, 'anagram', 'nagaram'))
        self.assertFalse(Solution.isAnagram(self, 'car', 'rat'))

        self.assertTrue(Solution.isAnagram(self, 'angel', 'glean'))
        self.assertFalse(Solution.isAnagram(self, 'hello', 'not hello'))


        self.assertTrue(Solution.isAnagram(self, 'players', 'parsley'))
        self.assertFalse(Solution.isAnagram(self, 'dog', 'cat'))

        self.assertFalse(Solution.isAnagram(self, "aacc" , "ccac"))



if __name__=='__main__':
    unittest.main()