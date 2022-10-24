// 1. dash-case(kebab-case) => html, css 사용
// 2. snake_case
// 3. camelCase === lowerCamelCase (JS 주로 활용)
// 4. PascalCase === UpperCamelCase (JS class명)
// 5. UPPER_SNAKE_CASE => 절대 변하면 안 될 것 같은 상수들

// 변수 선언
var a // 옛날 거
let b // 많이 쓰는 거 재할당 가능
const c // 변하지 마  재할당 불가능 (API ko-kr 등에 사용)

// 안 된다
console.log(bar)
let bar;

// 된다
console.log(foo)
var foo;
// ㄴ var의 호이스팅? 문제? 애를 죽여도 어디선가 살아서 나타날 수 있음