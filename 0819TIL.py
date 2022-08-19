# 재귀 부분집합
def powerset(idx):
    if idx == len(check):
        print(*check)
        result = []
        for j in range(len(check)):
            if check[j] == 1:
                result.append(arr[j])
        print(result)
        return
    for i in range(2): # 1과 0으로 표현하므로 무조건 range(2)
        check[idx] = i
        powerset(idx + 1)


arr = ['A', 'B', 'C', 'D', 'E']
check = [0] * len(arr)
powerset(0)

# 순열
arr = ['A', 'B', 'C']
sel = [0, 0, 0]
check = [0, 0, 0]


def perm(depth):  # 각자 뎁스에서는? 꿈안의 꿈(인셉션)-- ㅡ
    if depth == 3:  # 최고 뎁스에 도달했으면?
        print(sel)  # print
        return

    for i in range(3):  # 3번의 화살표 떨어트릴 기회
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth] = arr[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1)
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)

perm(0)