#리스트 속 딕셔너리의 키 값으로 정렬하고 뒤에서부터 가져오기
results = [
    {'name':'a', 'vote_average':2, 'age':16}, 
    {'name':'b', 'vote_average':3, 'age':20}, 
    {'name':'c', 'vote_average':1, 'age':66}
    ]
results = sorted(results, key=lambda x : x['vote_average']) #
print(results[-1:-6:-1]) #뒤에서부터 5개를 뽑으려면 맨 뒤에 -1을 써줘야 함! / , reverse=True로 하고 [0, 5]해도 된다.
# sorted(리스트, 기타) /값을 일시적으로 가짐, a=[], b=sorted[a] a!=b
# 리스트.sort()  ()안에 리버스랑 키 올 수 있따. /리스트를 아예 바꿔버림

#sorted(results, key=lambda (리스트 요소) : (리스트 요소가 딕셔너리 였으니까 딕셔너리의)[키값])
#키값을 기준으로 정렬한다. 근데 오름차순