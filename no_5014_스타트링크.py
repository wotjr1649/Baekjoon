# 5014 스타트링크
import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(current_point: int, end_point: int, visit: list):
    queue, visit[current_point] = deque([(current_point)]), 1
    while queue:
        current_point = queue.popleft()
        if current_point == end_point:
            return visit[current_point] - 1
        for i in [current_point + U, current_point - D]:
            if 1 <= i <= F and not visit[i]:
                visit[i] = visit[current_point] + 1
                queue.append(i)
    if not visit[end_point]:
        return "use the stairs"


F, S, G, U, D = map(int, input().split())
visit = [0] * (F + 1)
print(bfs(S, G, visit))
