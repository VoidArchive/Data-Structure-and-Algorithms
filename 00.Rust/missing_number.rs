impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut xor: i32 = 0;
        let n = nums.len();
        for n in 0..=n{
            xor ^= n as i32;
        }
        for n in nums{
            xor ^= n;
        }
        xor
    }
}