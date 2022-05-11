"use strict";
var twoSum = function(nums, target) {
    let map = {};

    for(const [i, number] of nums.entries()){
        let diff = target - number;
        if(diff in map){
            return [map[diff],i];
        }
        map[number] = i;
    }
    return NaN
};
console.log(twoSum([2,7,11,15],4))