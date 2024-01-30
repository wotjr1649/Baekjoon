# 13460 구슬 탈출 2
import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(RB):
    queue, visit, count = deque([RB]), [RB], 0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if count > 10:
                print(-1)
                return
            if data[rx][ry] == "O":
                print(count)
                return
            for i in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if data[nrx][nry] == "#":
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if data[nrx][nry] == "O":
                        break
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if data[nbx][nby] == "#":
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if data[nbx][nby] == "O":
                        break
                if data[nbx][nby] == "O":
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visit:
                    queue.append((nrx, nry, nbx, nby))
                    visit.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)


N, M = map(int, input().split())
data, B, R = [], None, None
visit = [[0] * (M) for _ in range(N)]
for i in range(N):
    data.append(list(map(str, input().strip())))
    if not B and "B" in data[i]:
        B = (i, data[i].index("B"))
    if not R and "R" in data[i]:
        R = (i, data[i].index("R"))

bfs(R + B)  # type: ignore
