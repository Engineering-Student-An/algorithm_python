
# DFS 재귀 함수 => Stack
def DFS(graph, v, visited):
    visited[v] = 1                  # 해당 노드 방문 체크
    print(v, end=' ')               # 방문 노드 출력
    for i in graph[v]:              # 인접 리스트에 저장된 연결된 노드
        if visited[i] == 0:         # 인접 노드에 방문하지 않았다면
            DFS(graph, i, visited)  # DFS 재귀 호출

# 그래프의 인접 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 방문 체크용 리스트
visited =[0] * 9

# DFS 시작
DFS(graph, 1, visited)