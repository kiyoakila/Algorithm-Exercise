// for both exercises, the id of the object you're searching for is given to you
// as integer. return the whole object that you're looking for
//
// it's up to you what to return if the object isn't found (we're not testing that)

function linearSearch(id, array) {
  // code goes here
}

// recursive
function binarySearch(id, A) {
  if (A.length == 1) {
    return A[0].id == id ? A[0] : undefined;
  }
  const mid = Math.floor(A.length / 2);
  if (A[mid].id == id) {
    return A[mid];
  } else if (A[mid].id < id) {
    return binarySearch(id, A.slice(mid));
  } else if (A[mid].id > id) {
    return binarySearch(id, A.slice(0, mid));
  }
}

// iterative
function binarySearch(id, A) {
  let min = 0;
  let max = A.length;
  while (min <= max) {
    const mid = Math.floor((min + max) / 2);
    if (A[mid].id < id) {
      min = mid + 1;
    } else if (A[mid].id > id) {
      max = mid - 1;
    } else {
      return A[mid];
    }
  }
  return undefined;
}

// unit tests
// do not modify the below code
test.skip('linear search', function () {
  const lookingFor = { id: 5, name: 'Brian' };
  expect(
    linearSearch(5, [
      { id: 1, name: 'Sam' },
      { id: 11, name: 'Sarah' },
      { id: 21, name: 'John' },
      { id: 10, name: 'Burke' },
      { id: 13, name: 'Simona' },
      { id: 31, name: 'Asim' },
      { id: 6, name: 'Niki' },
      { id: 19, name: 'Aysegul' },
      { id: 25, name: 'Kyle' },
      { id: 18, name: 'Jem' },
      { id: 2, name: 'Marc' },
      { id: 51, name: 'Chris' },
      lookingFor,
      { id: 14, name: 'Ben' },
    ])
  ).toBe(lookingFor);
});

test.skip('binary search', function () {
  const lookingFor = { id: 23, name: 'Brian' };
  expect(
    binarySearch(23, [
      { id: 1, name: 'Sam' },
      { id: 3, name: 'Sarah' },
      { id: 5, name: 'John' },
      { id: 6, name: 'Burke' },
      { id: 10, name: 'Simona' },
      { id: 12, name: 'Asim' },
      { id: 13, name: 'Niki' },
      { id: 15, name: 'Aysegul' },
      { id: 17, name: 'Kyle' },
      { id: 18, name: 'Jem' },
      { id: 19, name: 'Marc' },
      { id: 21, name: 'Chris' },
      lookingFor,
      { id: 24, name: 'Ben' },
    ])
  ).toBe(lookingFor);
});
