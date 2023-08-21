
# 변수 생성 및 입력
INF = 999999

n, m = map(int, input().split())
money = list()
result = [INF] * 10001
result[0] = 0

for i in range(n):
    temp = int(input())
    money.append(temp)

# 다이나믹 프로그래밍 (바텀업)
for i in range(1,m+1):
    minimum = result[i]
    for j in money:
        if i-j>=0:
            minimum = min(minimum, result[i-j]+1)
    result[i] = minimum

if result[m] == INF:
    print(-1)
else:
    print(result[m])