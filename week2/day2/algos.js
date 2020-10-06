/*
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

// const str1 = "abcABC"
// const expected1 = "abcABC"

// const str2 = "helloo"
// const expected2 = "helo"

// const str3 = "helloo world helloo world helloo world"
// const expected3 = "helo wrd"

function stringDedupe(str) {
  // set up
  var returnString = ""
  var seen = {
    // h: true,
    // e: true,
    // l: true,
    // o: true,
    // ' ': true,
    // w: true,
  }
  // repeating
  for (let i = 0; i < str.length; i++) {
    // console.log(str[i])
    var letter = str[i]
    // if it doesn't exists in the obj
    // console.log("seen.hasOwnProperty(letter): ", seen.hasOwnProperty(letter))
    // if (!seen.hasOwnProperty(letter)) {
    if (seen.hasOwnProperty(letter) == false) {
      seen[letter] = true
      returnString += letter
    }
    // add the key
  }
  // clean
  // console.log(seen)
  console.log(returnString)
  return returnString
}

// stringDedupe(str3)
/* ******************************************************************************** */

/*
  Given a string containing space separated words
  Reverse each word in the string.

  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello"
const expected1 = "olleh"

const str2 = "hello world"
const expected2 = "olleh dlrow"

const str3 = "abc def ghi"
const expected3 = "cba fed ihg"

function reverseWords(str) {
  var finalStringArray = []
  // split the string
  var splitted = str.split(" ")
  // console.log("splitted: ", splitted)

  for (let i = 0; i < splitted.length; i++) {
    // split the words into characters
    // console.log("splitted[i]: ", splitted[i])
    var chars = splitted[i].split("")
    // console.log("chars: ", chars)
    // reverse the characters
    var reversedChars = chars.reverse()
    // console.log("reversedChars: ", reversedChars)
    // join the characters
    var reversedStr = reversedChars.join("")
    // console.log("reversedStr: ", reversedStr)
    finalStringArray.push(reversedStr)
  }
  // join the string
  return finalStringArray.join(" ")
}

console.log(reverseWords(str3))
