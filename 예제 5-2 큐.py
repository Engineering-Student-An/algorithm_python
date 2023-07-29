from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append((4,5))
queue.popleft()
print(queue)
queue.pop() # 마지막에 들어온 숫자 제거
print(list(queue))