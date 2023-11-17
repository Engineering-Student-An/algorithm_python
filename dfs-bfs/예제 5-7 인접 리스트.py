adj_list = list([] for i in range(4))

# 노드 1에 연결된 노드 정보 저장 (노드, 가중치)
adj_list[1].append((2, 7))

# 노드 2에 연결된 노드 정보 저장 (노드, 가중치)
adj_list[2].append((3, 2))

# 노드 3에 연결된 노드 정보 저장 (노드, 가중치)
adj_list[3].append((1, 3))
adj_list[3].append((2, 4))

print(adj_list)


