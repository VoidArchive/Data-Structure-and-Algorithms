impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let x_str = x.abs().to_string().chars().rev().collect::<String>();
        if let Ok(y) = x_str.parse::<i32>(){
            x.signum() * y
        }else{
            0
        }    
    }
}