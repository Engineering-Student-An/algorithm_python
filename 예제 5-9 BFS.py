from collections import deque

# BFS 함수 => Queue 사용
def BFS(graph, start, visited):
    # 시작 노드를 큐에 삽입
    queue = deque([start])
    # 시작 노드 방문 체크
    visited[start]=True
    while queue :                   # 큐가 비어 있지 않을 때 까지
        v = queue.popleft()         # 큐에서 노드를 꺼냄
        print(v, end=' ')           # 꺼낸 노드 출력
        for i in graph[v]:          # 꺼낸 노드의 인접 노드에 대해서 반복
            if not visited[i]:      # 인접 노드가 방문 이전이라면
                queue.append(i)     # 큐에 인접 노드 삽입
                visited[i] = True   # 인접 노드 방문 체크

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
visited = [False] * 9

# BFS 시작
BFS(graph, 1, visited)