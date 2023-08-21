# 변수 생성
INF = 999999999         # 무한대 정의

# 입력
n = int(input())

# 다이나믹 프로그래밍 (바텀업 방식)
result = [INF] * (n+1)  # 0에서 1로 만드는 연산 횟수 : x (무한대)
result[1] = 0       # 1에서 1로 만드는 연산 횟수 : 0
for i in range(2, n+1):
    rule_a = (i % 5 == 0) * int(i / 5) + (i % 5 != 0) * 0
    rule_b = (i % 3 == 0) * int(i / 3) + (i % 3 != 0) * 0
    rule_c = (i % 2 == 0) * int(i / 2) + (i % 2 != 0) * 0
    rule_d = i - 1
    result[i] = min(result[rule_a], result[rule_b], result[rule_c], result[rule_d]) + 1

print(result[n])