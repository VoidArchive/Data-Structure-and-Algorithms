import unittest
from contains_duplicate import Solution

class TestDuplicate(unittest.TestCase):

    def test_contains_duplicate(self):
        self.assertTrue(Solution.containsDuplicate(self,[1,2,3,1]),msg="Contains Duplicate")
        self.assertFalse(Solution.containsDuplicate(self, [1,2,3,4]), msg="Doesn't Contains Duplicate")
        self.assertTrue(Solution.containsDuplicate(self, [1,1,1,3,3,4,3,2,4,2]), msg="Contains Duplicate")
    
    def test_contains_duplicate_hashset(self):
        self.assertTrue(Solution.containsDuplicate_hashset(self,[1,2,3,1]),msg="Contains Duplicate")
        self.assertFalse(Solution.containsDuplicate_hashset(self, [1,2,3,4]), msg="Doesn't Contains Duplicate")
        self.assertTrue(Solution.containsDuplicate_hashset(self, [1,1,1,3,3,4,3,2,4,2]), msg="Contains Duplicate")

if __name__=='__main__':
    unittest.main()