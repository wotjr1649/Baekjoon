# 1389 케빈 베이컨의 6단계 법칙
import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(start, visit):
    queue = deque([start])
    visit[start] = 1

    while queue:
        a = queue.popleft()
        for i in data[a]:
            if not visit[i]:
                visit[i] = visit[a] + 1
                queue.append(i)

    return sum(visit) - visit[start] - 4


N, M = map(int, input().split())
data, result = [[] for _ in range(N + 1)], []

for _ in range(N):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(1, N + 1):
    visit = [0] * (N + 1)
    result.append(bfs(i, visit))

print(result.index(min(result)) + 1)
