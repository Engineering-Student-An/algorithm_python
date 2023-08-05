
# 입력
n, search = map(int, input().split())
array = list(map(int, input().split()))

# 반복문
start = 0
end = n-1
result = -1
while start<=end:
    middle = (start + end) // 2
    if array[middle] == search:
        result = middle
        break
    elif array[middle] > search:
        end = middle-1
    else :
        start = middle+1

if result == -1 :
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)