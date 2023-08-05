
# 입력
n = int(input())
arr = list(map(int,input().split()))

m = int(input())
find = list(map(int,input().split()))

# 계수 정렬
check = [0] * (max(arr) + 1)
for i in range(n):
    check[arr[i]] += 1

for i in find:
    if check[i] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')