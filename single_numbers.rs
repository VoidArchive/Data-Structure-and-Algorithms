impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
       let result = 0;
       for i in nums{
           result = i ^ result;
       }
       return result;

    }
}