

n,m = map(int,input().split())
card=list()

for i in range(n):
    row = list(map(int,input().split()))
    card.append(row)

for i in range(n):
    card[i].sort()

max_result = 0

for i in range(n):
    if card[i][0] > max_result : max_result = card[i][0]

print(max_result)
