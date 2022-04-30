import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        
        self.assertEqual(Solution.twoSum(self, [2,7,10,11], 9), [0,1])
        self.assertEqual(Solution.twoSum(self, [3,2,4], 6), [1,2])


if __name__=='__main__':
    unittest.main()