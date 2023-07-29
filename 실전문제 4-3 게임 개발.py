import copy as copy
# 입력, 변수 선언
row, col = map(int, input().split())
y, x, d = map(int, input().split())
array = list()

for i in range(row):
    tmp = list(map(int, input().split()))
    array.append(tmp)

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
check = copy.deepcopy(array)
result = 1

# 메인 함수
check[y][x] = 1                     # 첫 시작점 체크
turn = 0
while True:
    # 규칙 1 : 왼쪽으로 회전
    d = (d+1) % 4
    tmpy = y+dir[d][0]
    tmpx = x+dir[d][1]

    # 규칙 2 : 가보지 않은 칸 존재 o
    if check[tmpy][tmpx]==0 and array[tmpy][tmpx]==0:
        result += 1
        check[tmpy][tmpx] = 1
        y = tmpy
        x = tmpx
        turn = 0

    # 규칙 2 : 가보지 않은 칸 존재 x
    else:
        turn += 1

    # 규칙 3 : 네 방향 모두 가본 칸이거나 바다인 경우
    if turn == 4:
        tmpy = y-dir[d][0]
        tmpx = x-dir[d][1]
        if array[tmpy][tmpx]==0:
            y = tmpy
            x = tmpx
        else:
            break
        turn = 0

print(result)

