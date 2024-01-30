# 3055 탈출
import sys
from collections import deque

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C = map(int, input().split())
data = [list(map(str, input().strip())) for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [[0] * C for _ in range(R)]
queue = deque()

for i in range(R):
    for j in range(C):
        if data[i][j] == "S":
            queue.append((i, j))
        if data[i][j] == "D":
            Dx, Dy = i, j

for i in range(R):
    for j in range(C):
        if data[i][j] == "*":
            queue.append((i, j))


def bfs(Dx: int, Dy: int) -> str:
    while queue:
        x, y = queue.popleft()
        if data[Dx][Dy] == "S":
            return visit[Dx][Dy]  # type: ignore

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if (data[nx][ny] == "." or data[nx][ny] == "D") and data[x][y] == "S":
                    data[nx][ny], visit[nx][ny] = "S", visit[x][y] + 1
                    queue.append((nx, ny))
                elif (data[nx][ny] == "." or data[nx][ny] == "S") and data[x][y] == "*":
                    data[nx][ny] = "*"
                    queue.append((nx, ny))

    return "KAKTUS"


print(bfs(Dx, Dy))  # type: ignore
