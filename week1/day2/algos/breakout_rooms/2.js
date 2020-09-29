// RIOT Walk

// Repeat
// Input
// Output
// Test

// Walk-through

var members = [
  "Steven Wittkopf",
  "Kyle Howell",
  "Stephen Lebel",
  "Adam Humecky",
  "Sean Sarreal",
]

// ************************************************

/*
  String: Reverse

  Implement reverseString(str)
  Input: 'abc'
  Output: 'cba'
*/

function reverseString(str) {
  let output = ""
  for (let i = str.length - 1; i >= 0; i--) {
    output += str[i]
  }
  return output
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
  let newWord, result
  newWord = true
  result = ""

  for (let i = 0; i < str.length; i++) {
    if (str[i] == " ") {
      newWord = true
    } else if (newWord) {
      result += str[i].toUpperCase()
      newWord = false
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
  return str1.toUpperCase() == str2.toUpperCase()
}

var caseInsensitiveCompareTestCaseA = "ABC"
var caseInsensitiveCompareTestCaseB = "abc"
var caseInsensitiveCompareReturnValue = stringAcronym(
  caseInsensitiveCompareTestCaseA,
  caseInsensitiveCompareTestCaseB
)
console.log(caseInsensitiveCompareReturnValue) // true
