
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0
while end>=start:
    middle = (start + end) // 2
    sum = 0
    for i in arr:
        if i > middle:
            sum += (i-middle)

    if sum < m:
        end = middle - 1
    else:
        result = middle
        start = middle + 1
print(result)
