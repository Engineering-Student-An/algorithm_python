
# 변수 생성 및 입력
n = int(input())
result = [0] * 1001

# 다이나믹 프로그래밍 (바텀업)
result[0] = result[1] = 1
for i in range(2, n+1):
    result[i] = (result[i-2] * 2 + result[i-1]) % 796796

print(result[n])