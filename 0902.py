# 연습문제 1 - 후위 표기법
# T = int(input())
# for tc in range(1, T + 1):
#     problem = input()
#     stack = []
#     answer = []
#     for i in problem:
#         if i.isdigit():
#             answer.append(i)
#         else:
#             stack.append(i)
#     while stack:
#         a = stack.pop()
#         answer.append(a)
#     print(f'#{tc} {"".join(answer)}')

# 연습문제 1 - Extra
T = int(input())
operator = {
    '+': 0, '-': 0, '*': 1, '/': 1
}
for tc in range(1, T + 1):
    problem = input()
    stack = []
    answer = []
    for i in problem:
        if i.isdigit():
            answer.append(i)
        else:
            if stack and operator[i] > operator[stack[-1]]:
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    stack.pop()
                stack.pop()
            elif stack:
                while stack and stack[-1] != '(' and i != '(' and operator[i] <= operator[stack[-1]]:
                    answer.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
    answer += stack
    print(*answer)