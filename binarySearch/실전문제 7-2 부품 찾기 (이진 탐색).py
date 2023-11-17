
# 입력
n = int(input())
arr = list(map(int,input().split()))
arr.sort()  # 리스트를 오름차순 정렬

m = int(input())
find = list(map(int,input().split()))

# 이진 탐색 함수
def binary_search(arr, search, start, end):
    if start>end:
        return 'no'
    middle = (start + end) // 2
    if arr[middle] == search:
        return 'yes'
    elif arr[middle] > search:
        return binary_search(arr, search, start, middle-1)
    else:
        return binary_search(arr, search, middle+1, end)

# 메인 함수
for i in find:
    print(binary_search(arr, i, 0, n-1), end=' ')



