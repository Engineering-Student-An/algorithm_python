n=int(input('수를 입력하세요 : '))

# 반복문
result = 1
for i in range(1, n+1):
    result *= i

print("반복문 결과 :",result)

# 재귀함수
def factorial(n):
    if n<=1: return 1
    return n*factorial(n-1)
print("재귀함수 결과 :",factorial(n))
