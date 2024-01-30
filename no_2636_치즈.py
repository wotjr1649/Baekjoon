# 2636 치즈
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs() -> int:
    queue = deque([(0, 0)])
    melt = deque([])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if data[nx][ny]:
                    melt.append((nx, ny))
                else:
                    queue.append((nx, ny))  # type: ignore
    for x, y in melt:
        data[x][y] = 0
    return len(melt)


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cnt, time = sum([sum(i) for i in data]), 1

while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if not cnt:
        print(time, meltCnt, sep="\n")
        break
    time += 1
