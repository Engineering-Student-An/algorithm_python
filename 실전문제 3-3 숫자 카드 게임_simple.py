

n,m = map(int,input().split())

max_result = 0
for i in range(n):
    row = list(map(int,input().split()))
    row_min = min(row)
    if row_min > max_result :
        max_result = row_min

print(max_result)
