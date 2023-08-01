
# 입력
n = int(input())
array=list()
for i in range(n):
    name, score = input().split()
    score = int(score)
    array.append( (name, score) )

# 정렬 라이브러리
array.sort(key=lambda x: x[1])
for i in array:
    print(i[0], end=' ')