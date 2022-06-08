/*

  Quick Sort!
  
  Name your function quickSort.
  
  Quick sort should grab a pivot from the end and then separate the list (not including the pivot)
  into two lists, smaller than the pivot and larger than the pivot. Call quickSort on both of those
  lists independently. Once those two lists come back sorted, concatenate the "left" (or smaller numbers)
  list, the pivot, and the "right" (or larger numbers) list and return that. The base case is when quickSort
  is called on a list with length less-than-or-equal-to 1. In the base case, just return the array given.

*/

function quickSort(A) {
  // base case
  if (A.length < 2) {
    return A;
  } else {
    const pivot = A.pop();
    // L is the container for all the elements smaller than pivot
    const L = [];
    // for larger elements
    const R = [];
    for (let i = 0; i < A.length; i++) {
      if (A[i] < pivot) {
        L.push(A[i]);
      } else {
        R.push(A[i]);
      }
    }
    // conquer L and R recursively
    return [...quickSort(L), pivot, ...quickSort(R)];
    // const sortedL = quickSort(L);
    // const sortedR = quickSort(R);
    // return sortedL.concat(pivot, sortedR);
  }
}

// unit tests
// do not modify the below code
test.skip('quickSort', function () {
  const input = [10, 8, 2, 1, 6, 3, 9, 4, 7, 5];
  const answer = quickSort(input);

  expect(answer).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
});
