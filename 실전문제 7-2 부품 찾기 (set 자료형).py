
# 입력
n = int(input())
arr = set(map(int,input().split()))

m = int(input())
find = list(map(int,input().split()))

print(arr)

for i in find:
    if i in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')