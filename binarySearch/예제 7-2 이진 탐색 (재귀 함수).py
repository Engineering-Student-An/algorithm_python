
# 입력
n, search = map(int, input().split())
array = list(map(int, input().split()))


# 재귀 함수 구현
def recursive(array, search, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    if array[middle] == search :
        return middle
    elif array[middle] > search :
        return recursive(array, search, start, middle-1)
    elif array[middle] < search :
        return recursive(array, search, middle+1, end)


# 재귀 함수 호출
result = recursive(array, search, 0, n-1)
if result == -1 :
    print("원소가 존재하지 않습니다.")
else:
    print(int(result)+1)