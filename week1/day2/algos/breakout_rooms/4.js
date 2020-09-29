// RIOT Walk

// Repeat
// Input
// Output
// Test

// Walk-through

var members = ["Donna", "Vikram", "Zach", "Ali", "Ling"]

// ************************************************

/*
  String: Reverse

  Implement reverseString(str)
  Input: 'abc'
  Output: 'cba'
*/

function reverseString(str) {
  // set up
  var newString = ""

  // do some repetative work
  //        start,             stop,  step
  // for (var i = 0; i < str.length; i++) {
  //          2                 2>= 0   -
  for (var i = str.length - 1; i >= 0; i--) {
    newString += str[i]
    // newString = newString + str[i]
  }

  // clean up or return
  return newString
}

var reverseStringTestCase = "abc"
var reverseStringReturnValue = reverseString(reverseStringTestCase)
console.log(reverseStringReturnValue) // 'cba'

// ************************************************
/*
  Acronyms

  Create a function that, given a string, returns the string’s acronym
  (first letter of each word capitalized).

  Do it with .split first if you need to, then try to do it without

  input: 'The quick brown fox, jumped over the lazy dog.'
  output: 'TQBFJOTLD'

  Hint: string.toUpperCase()

*/

function stringAcronym(str) {
array=str.split(" ");
arr=[]
for(var i=0; i <= array.length; )
}

var stringAcronymTestCase = "The quick brown fox, jumped over the lazy dog."
var stringAcronymReturnValue = stringAcronym(stringAcronymTestCase)
console.log(stringAcronymReturnValue) // 'TQBFJOTLD'

// ************************************************

/*
  Case insensitive string comparison

  const test1StrA = "ABC"
  const test1StrB = "abc"
  caseInsensitiveCompare(test1StrA, test1StrB) // Output: true
*/

functio()n caseInsensitiveCompare(str1, str2) {
  // code here
}

var caseInsensitiveCompareTestCaseA = "ABC"
var caseInsensitiveCompareTestCaseB = "abc"
var caseInsensitiveCompareReturnValue = stringAcronym(
  caseInsensitiveCompareTestCaseA,
  caseInsensitiveCompareTestCaseB
)
console.log(caseInsensitiveCompareReturnValue) // true
