# 변수 생성 및 입력
n, m = map(int, input().split())    # N, M 입력

array = list()                      # array : 입력을 문자열의 형태로 받음
for i in range(n):
    array.append(list(map(int,input())))

check = list([False]*m for i in range(n))       # check : 방문 여부 체크 리스트
linked_list = list([0]*m for i in range(n))     # linked_list : 인접 리스트

result = 0  # 최종 결과

# 인접 리스트 만드는 함수
def make_linked_list(array, linked_list):
    dx = [-1, +1, 0, 0]     # 상하좌우 순 x 좌표 변화
    dy = [0, 0, -1, +1]     # 상하좌우 순 y 좌표 변화
    for i in range(n):
        for j in range(m):
            temp = list()
            for k in range(4):  # 상하좌우 연결 상태 체크
                if i+dx[k]>=0 and i+dx[k]<n and \
                    j+dy[k]>=0 and j+dy[k]<m and \
                    array[i+dx[k]][j+dy[k]] == 0 : temp.append( (i+dx[k], j+dy[k]) )
            linked_list[i][j] = temp

# DFS
def DFS(linked_list, ind_i, ind_j, check):
    check[ind_i][ind_j] = True
    for i,j in linked_list[ind_i][ind_j]:
        if check[i][j] == False:
            DFS(linked_list, i, j, check)


make_linked_list(array, linked_list)
for i in range(n):
    for j in range(m):
        if array[i][j] == 0 and check[i][j] == False:
            result+=1
            DFS(linked_list, i, j, check)

print(result)