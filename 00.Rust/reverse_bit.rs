impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut result = 0;
        for i in 0..32{
            let bit = x & 1 << i;
            let travel = (31 - i as i32) - i as i32;
            if travel > 0{
                result |= bit << travel;
            } 
            else{
                result |= bit >> -travel;
            }

            }
            result
        }    
    }
