// // 선언식 : 익명 함수 불가능, 호이스팅 있음
// console.log(add(7, 2))

// function add(num1, num2) {
//   return num1 + num2
// }

// // 표현식 : 익명함수 가능, 호이스팅 없음 권장
// const sub = function (num1, num2) {
//   return num1 - num2
// }
// console.log(sub(7, 2))

// const greeting = function (name = 'Anonimous') {
//   return `Hi ${name}`
// }
// console.log(greeting())

// // 화살표 함수
// const gre = (name) => `Hi ${name}`

// const g = name => `Hi ${name}`

// // 즉시 실행 함 : 1회성 사용
// (function(num) { return num ** 3})(2) //8
// ((num) => num ** 3)(2) //8

// const numbers = [1, 2, 3, 4, 5]
// numbers.reverse()
// numbers.pop()
// numbers.push(100)
// console.log(numbers.includes(1))
// console.log(numbers.includes(77))
// console.log(numbers.indexOf(3))
// console.log(numbers.indexOf(77))
// console.log(numbers.join())
// console.log(numbers.join(''))
// console.log(numbers.join('-'))

// forEach
const colors = ['r', 'b', 'g']

colors.forEach((color) => {
  console.log(color)
}) 
// === colors.forEach((color) => console.log(color))

// map
const newArry = colors.map((color) => {
  return color + color
})
console.log(newArry)

// filter
const product = [
  {name: 'cucumber', type: 'vegi'},
  {name: 'carrot', type: 'vegi'},
  {name: 'banana', type: 'fruit'},
  {name: 'apple', type: 'fruit'}
]

const newArr = product.filter((product) => {
  return product.type === 'fruit'
})
console.log(newArr)

// reduce
const numbers = [90, 80, 70, 100]
const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length
console.log(avgNum)

// find

// some

// every

// json파일 변환 (string - dict)
JSON.stringify(dataToJson)
JSON.parse(jsonToData)