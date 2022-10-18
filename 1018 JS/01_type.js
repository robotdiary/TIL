// 데이터 종류 (자료형) -> JS는 데이터 기준으로 사고

/*
  Primitive Types
  1. Number
  2. String
  3. Empty (NULL, Undifined)
  4. Boolean
*/

// String
let myName = 'alex'
let greeting = `Hello, my name is ${myName}`
console.log(greeting)

console.log('안녕' + '하쇼')

console.log('안녕~ ' + 3 + '살 아가') // 형변환

// Number
console.log(
    'Number Types: ',
    Infinity, -Infinity, NaN
)

// Empty 
console.log(undefined, null)

// Boolean
console.log(true, false)