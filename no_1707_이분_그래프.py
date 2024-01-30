# 1707 이분 그래프
import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(node):
    global error
    visit[node] = 1

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visit[i]:
                visit[i] = -1 * visit[node]
                queue.append(i)
            elif visit[i] == visit[node]:
                error = True
                return


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph, visit = [[] for _ in range(V + 1)], [0] * (V + 1)
    error, queue = False, deque()

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visit[i] and not error:
            queue.append(i)
            bfs(i)

    print("YES" if not error else "NO")
