/*
  Given an arr and a separator string, output a string of every item in the array separated by the separator.

  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

// var arr2 = [1, 2, 3]
// var separator2 = "-"
// var expected2 = "1-2-3"

// var arr3 = [1, 2, 3]
// var separator3 = " - "
// var expected3 = "1 - 2 - 3"

// var arr4 = [1]
// var separator4 = ", "
// var expected4 = "1"

// var arr5 = []
// var separator5 = ", "
// var expected5 = ""

var arr1 = [1, 2, 3]
var separator1 = ", "
var expected1 = "1, 2, 3"

function join(arr, separator) {
  console.log(arr, separator)
  // set up
  var newString = ""
  // create a for loop
  for (var i = 0; i < arr.length - 1; i++) {
    // read each value in the array
    // add each value to the new string
    // with separator between each value
    newString += arr[i] + separator
    // newString = newString + arr[i] + separator
  }

  newString += arr[arr.length - 1]

  console.log(newString)
  // return new string
  return newString
}

join(arr1, separator1)
/* ******************************************************************************** */

/*
  String Encode

  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears.

  */

// var str1 = "aaaabbcddd"
// var expected1 = "a4b2c1d3"

// var str2 = ""
// var expected2 = ""

// var str3 = "aa"
// var expected3 = "a2"

// var str4 = "bbcc"
// var expected4 = "b2c2"

function encodeStr(str) {
  // code here
}

/* ******************************************************************************** */

/*
  String Decode
*/

// var str1 = "a3b2c1d3"
// var expected1 = "aaabbcddd"

function decodeStr(str) {
  // code here
}
