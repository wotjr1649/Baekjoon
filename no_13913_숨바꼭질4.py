# 13913 숨바꼭질 4

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def move(x):
    data, temp = [], x
    for _ in range(visited[x] + 1):
        data.append(temp)
        temp = check[temp]
    print(*data[::-1])


def bfs(x: int):
    queue = deque([(x)])
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[K])
            move(x)
            break
        for i in [x - 1, x + 1, 2 * x]:
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[x] + 1
                check[i] = x
                queue.append(i)  # type: ignore


MAX = 100_001
N, K = map(int, input().split())
visited, check = [0] * MAX, [0] * MAX

bfs(N)
