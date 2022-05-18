memo = new Map();

function fibo(num) {
  if (num == 1 || num == 0) {
    return num;
  }
  if (!(num in memo)) {
    memo[num] = fibo(num - 1) + fibo(num - 2);
  }
  return memo[num];
}

console.log(fibo(10));
console.log(fibo(9));
console.log(fibo(8));
console.log(fibo(7));
console.log(fibo(6));
console.log(fibo(5));
console.log(fibo(4));
console.log(fibo(3));
console.log(fibo(2));
console.log(fibo(1));
