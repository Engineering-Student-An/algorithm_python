
d = [0] * 100

# 피보나치 수열 함수
def fibo(n):
    print('**f(', n, ')', sep='', end=' ')      # 처음 호출되는 경우 앞에 **추가
    if n==1 or n==2:
        return 1
    if d[n] != 0:
        return d[n]
    print('f(', n, ')', sep='', end=' ')        # 값이 저장되어 있지 않은 경우 (값을 구해야 하는 경우)
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

print(fibo(6))