// const jinjin = {
//     lastName: 'kim',
//     firstName: 'jinny',
//     greeting: function () {
//         return `안녕하세요? ${this.lastName + this.firstName}입니다.`
//     }
// }
// // -----------------------------------------------------------------
// function greeting() {
//     return `안녕하세요? ${this.lastName + this.firstName}입니다.`
// }

// const bulbul = {
//     lastName: 'kim',
//     firstName: 'burri',
//     greeting
// }

const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  // solution 함수 완성 이동가능, 종점, 충전기개수, [충전 정류장 번호]
function solution(K, N, M, chargers) {
  let now = N
  let cnt = 0
  // 만약 현재 위치가 마지막 정류장 뒤면 충전 횟수 출력
  // 현재 위치 + K 안에 충전기가 있다면, 현재 위치는 맨 뒤 충전기
  // 현재 위치 + K 안에 충전기가 없다면 -1 출력
  for (now; now >= now-K; now--) {
    console.log(now)
    if (chargers.indexOf(now) === 1) {
      cnt += 1
    }
  }
//  console.log(cnt)
}
for (const input of inputs) {
  solution(...input)
}