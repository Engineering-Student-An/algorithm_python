
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)

result = 0

biggest_cnt = m//(k+1)*k + m%(k+1)

result += biggest_cnt * array[0]
result += (m-biggest_cnt) * array[1]

print(result)


