/*

  Implement a radix sort in a function called radixSort.

  You'll probably need several functions
  
  You can implement it using a binary or decimal based bucketing but I'd recommend the decimal based buckets because
  it ends up being a lot more simple to implement.

*/

function getDigit(num, place, len) {
  const s = String(num);
  L = s.length;
  // imagine filled up with len-L zeros
  const mod = len - L;
  // if exceed boundary (undefined), return 0
  return Number(s[place - mod]) || 0;
}

function findLongestLength(A) {
  let max = 0;
  for (const item of A) {
    const len = item.toString().length;
    max = len > max ? len : max;
  }
  return max;
}

function radixSort(A) {
  // calculate the length of the longerst number
  len = findLongestLength(A);
  // create 10 bukets for 10 digits.
  buckets = new Array(10).fill().map(() => []);
  // for loop from least significant digit to most sig digit
  for (let i = len - 1; i >= 0; i--) {
    // enqueue the item into buckets
    while (A.length) {
      const item = A.shift();
      // find the bucket
      const m = getDigit(item, i, len);
      // enqueue the item
      buckets[m].push(item);
    }
    // empty the bucket for each digit
    for (let j = 0; j < 10; j++) {
      while (buckets[j].length) {
        A.push(buckets[j].shift());
      }
    }
  }
  return A;
}

// unit tests
// do not modify the below code
test('radix sort', function () {
  test.skip('should sort correctly', () => {
    const nums = [
      20, 51, 3, 801, 415, 62, 4, 17, 19, 11, 1, 100, 1244, 104, 944, 854, 34,
      3000, 3001, 1200, 633,
    ];
    const ans = radixSort(nums);
    expect(ans).toEqual([
      1, 3, 4, 11, 17, 19, 20, 34, 51, 62, 100, 104, 415, 633, 801, 854, 944,
      1200, 1244, 3000, 3001,
    ]);
  });
  test.skip('should sort 99 random numbers correctly', () => {
    const fill = 99;
    const nums = new Array(fill)
      .fill()
      .map(() => Math.floor(Math.random() * 500000));
    const ans = radixSort(nums);
    expect(ans).toEqual(nums.sort());
  });
});
