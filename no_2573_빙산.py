# 2573 빙산
import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1  # type: ignore
    seaList = []
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not data[nx][ny]:
                    sea += 1
                elif data[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        data[x][y] = max(0, data[x][y] - sea)

    return 1


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
icy = [(i, j) for i in range(N) for j in range(M) if data[i][j]]
year, group = 0, 0

while icy:
    visited = [[0] * M for _ in range(N)]
    delList = []
    group = 0
    for i, j in icy:
        if data[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if not data[i][j]:
            delList.append((i, j))
    if group > 1:
        print(year)
        break

    icy = sorted(list(set(icy) - set(delList)))
    year += 1

if group < 2:
    print(0)

# icy = sorted([(i,j,data[i][j]) for i in range(N) for j in range(M) if data[i][j]], key = lambda x :x[2])
