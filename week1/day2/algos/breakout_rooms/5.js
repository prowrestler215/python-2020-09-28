// RIOT Walk

// Repeat
// Input
// Output
// Test

// Walk-through

var members = ["Thomas Hott", "Edward CHilders"]

// ************************************************

/*
  String: Reverse

  Implement reverseString(str)
  Input: 'abc'
  Output: 'cba'
*/

function reverseString(str) {
  var new_str = ""
  for (var i = str.length - 1; i >= 0; i--) {
    reverseStringTestCase += str[i]
  }
  return reverseStringTestCase
}

var reverseStringTestCase = "abc"
var reverseStringReturnValue = reverseString(reverseStringTestCase)
console.log(reverseStringReturnValue) // 'cba'

/*python code


def reverseString(str):
  return str[::-1]

txt = reverseString("abc")

print(txt)

*/

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
  var string = true
  var result = ""
  for (var i = 0; i < str.length; i++) {
    if (str[i == ""]) {
      string = true
    } else if (string) {
      result += str[i].toUpperCase()
      string = false
    }
  }
  return result
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

function caseInsensitiveCompare(str1, str2) {
  // code here
}

var caseInsensitiveCompareTestCaseA = "ABC"
var caseInsensitiveCompareTestCaseB = "abc"
var caseInsensitiveCompareReturnValue = stringAcronym(
  caseInsensitiveCompareTestCaseA,
  caseInsensitiveCompareTestCaseB
)
console.log(caseInsensitiveCompareReturnValue) // true
