position = input()
col = ord(position[0]) - int(96)
row = int(position[1])

# 8 x 8 로 구성된 체스판
dir_row = [-2, -2, -1, +1, +2, +2, -1, +1]
dir_col = [-1, +1, +2, +2, -1, +1, -2, -2]
cnt = 0

for i in range(8):
    next_col = col+dir_col[i]
    next_row = row+dir_row[i]
    if next_col >= 1 and next_col<=8 \
            and next_row>=1 and next_row<=8:
        cnt+=1

print(cnt)