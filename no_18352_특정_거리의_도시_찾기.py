# 18352 특정 거리의 도시 찾기
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def qsort(li) -> list:
    if len(li) <= 1:
        return li
    pivot, tail = li[0], li[1:]
    left_li = [x for x in tail if x <= pivot]
    right_li = [x for x in tail if x > pivot]
    return qsort(left_li) + [pivot] + qsort(right_li)


def bfs(x):
    queue = deque([x])
    visited[x] = 1
    answer = []
    while queue:
        x = queue.popleft()
        for i in data[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[x] + 1
                if distance[i] == K:
                    answer.append(i)
    if not answer:
        print(-1)
    else:
        print(*qsort(answer), sep="\n")


N, M, K, X = map(int, input().split())
data, visited, distance = (
    {i: [] for i in range(N + 1)},
    {i: 0 for i in range(N + 1)},
    {i: 0 for i in range(N + 1)},
)

for i in range(M):
    a, b = map(int, input().split())
    data[a].append(b)

bfs(X)
