# 9019  DSLR pypy3로 제출
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(x, visited):
    queue = deque([("", x)])

    while queue:
        command, x = queue.popleft()
        if x == B:
            return command
        for i in ["D", "S", "L", "R"]:
            if i == "D":
                reg = (x * 2) % 10000
            elif i == "S":
                reg = (x - 1) % 10000
            elif i == "L":
                reg = x // 1000 + (x % 1000) * 10
            else:
                reg = x // 10 + (x % 10) * 1000
            if not visited[reg]:
                visited[reg] = True
                queue.append((command + i, reg))  # type: ignore


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10001
    print(bfs(A, visited))
