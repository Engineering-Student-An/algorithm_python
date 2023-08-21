
# 변수 생성 및 입력
n = int(input())
array = list(map(int,input().split()))
result = [0] * 100

# 다이나믹 프로그래밍 (바텀업)
result[0] = array[0]
result[1] = max(array[0], array[1])
for i in range(2, n):
    result[i] = max(result[i-2] + array[i], result[i-1])

print(result[n-1])
