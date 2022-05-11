"use strict";

const isAlphaNumeric = str => /^[a-z0-9]+$/gi.test(str);


var isPalindrome = function(s) {
    let left = 0;
    let right = s.length -1;

    while(left < right){

        while((left < right) && !isAlphaNumeric(s[left])){
            left++;
        }
        while((left < right) && !isAlphaNumeric(s[right])){
            right--;
        }

        if(s[left].toLowerCase() != s[right].toLowerCase()){
            return false;
        }

        left++;
        right--;
    }
    return true;

    
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));