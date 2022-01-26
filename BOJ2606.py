M = int(input())
N = int(input())
arr = [[0]*(M+1) for _ in range(M+1)]

for i in range(N):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
visited = [0]*(M+1)


def bfs(V):
    answer = 0
    queue = [V]
    visited[V] = 1
    while queue:
        V = queue[0]
        queue.pop(0)
        for i in range(1, M+1):
            next = arr[V][i]
            if next == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                answer += 1
    return answer


print(bfs(1))
