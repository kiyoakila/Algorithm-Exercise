/*
  Write a function that performs mergesort
  Name the function mergeSort
  It will take in a array of numbers and return a sorted array numbers

  You'll need to write more than just one function
*/

const mergeSort = (A) => {
  // base case
  if (A.length == 1) {
    return A;
  } else {
    // break and merge
    const m = Math.floor(A.length / 2);
    const L = mergeSort(A.slice(0, m));
    const R = mergeSort(A.slice(m));
    return merge(L, R);
  }
};

function merge(A, B) {
  const C = [];
  while (A.length > 0 && B.length > 0) {
    // shift the smaller number to C
    C.push(A[0] < B[0] ? A.shift() : B.shift());
  }
  // better way: return C.concat(A,B)
  return C.concat(0 == A.length ? B : A);
}

// unit tests
// do not modify the below code
test.skip('merge sort', function () {
  const nums = [10, 5, 3, 8, 2, 6, 4, 7, 9, 1];
  const ans = mergeSort(nums);
  expect(ans).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
});
