use std::collections::HashMap;

impl Solution {
    fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hash_map: HashMap<i32, i32> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            match hash_map.get(num) {
                Some(&index) => return vec![index, i as i32],
                None => hash_map.insert(target - num, i as i32),
            };
        }
        vec![]
    }
}

fn main() {
    let v: Vec<i32> = vec![2, 7, 11, 15];

    let result = two_sum(v, 9);
    println!("{:?}", result);
}
