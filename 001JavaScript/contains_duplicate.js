const containsDuplicate = (nums) => {
  let a = [];
  for (let i of nums) {
    if (a.includes(i)) {
      return true;
    } else {
      a.push(i);
    }
  }
  return false;
};

console.log(containsDuplicate([3, 3]));

const setSolution = nums => {
  let hashSet = new Set(nums);
  return hashSet.size !== nums.length 
}

console.log(setSolution([3,3,2,3]))

const objectSolution = nums => {
  let testObj = {};
  for(let i of nums){
    if(testObj[i]) return true;
    else testObj[i] = true;
  }
  return false;
}

console.log(objectSolution([1,3]))