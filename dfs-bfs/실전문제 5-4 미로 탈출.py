from collections import deque

n, m = map(int, input().split())

array=list()
for i in range(n):
    array.append(list(map(int, input())))

check = list([False]*m for i in range(n))
check[0][0]=1
linked_list = list([0]*m for i in range(n))

queue = deque()

def make_linked_list(array, linked_list):
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    for i in range(n):
        for j in range(m):
            temp = list()
            for k in range(4):
                if i+dx[k]>=0 and i+dx[k]<n and \
                    j+dy[k]>=0 and j+dy[k]<m and \
                    array[i+dx[k]][j+dy[k]] == 1 :
                        temp.append( (i+dx[k], j+dy[k]) )
            linked_list[i][j]=temp

def BFS(array, check):
    global queue, result
    check[0][0] = True
    queue.append( (0,0) )
    while queue:
        i,j = queue.popleft()
        if i==n-1 and j==m-1: break
        result = check[i][j]+1
        for ind_i, ind_j in linked_list[i][j]:
            if check[ind_i][ind_j] == False:
                queue.append((ind_i,ind_j))
                check[ind_i][ind_j] = result

make_linked_list(array, linked_list)
BFS(array, check)
print(check[n-1][m-1])