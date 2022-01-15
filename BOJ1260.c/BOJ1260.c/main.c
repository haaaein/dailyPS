#include <stdio.h>
#define MAX 1001

int graph[MAX][MAX];
int visited[MAX * MAX];

void dfs(int v, int N) //깊이 우선 탐색
{
    visited[v] = 1;
    printf("%d ", v);
    
    for (int u = 1; u <= N; u++)
        if (graph[v][u] && !visited[u])
            dfs(u, N);
}

void bfs(int v, int N) //너비 우선 탐색
{
    int front = -1, rear = -1;
    int queue[MAX * MAX] = {0};
    
    rear++;
    queue[rear] = v;
    
    visited[v] = 1;
    printf("%d ", v);
    
    while (front < rear) {
        front++;
        int nextV = queue[front];
        
        for (int d = 1; d <= N; d++) {
            if (!visited[d]&& graph[nextV][d]) {
                printf("%d ", d);
                rear++;
                visited[d] = 1;
                queue[rear] = d;
            }
        }
    }
}

void init(int N)
{
    printf("\n");
    for (int i = 1; i <= N; i++)
        visited[i] = 0;
}

int main()
{
    int N = 0, M = 0, V = 0;
    int r, c;
    
    scanf("%d %d %d", &N, &M, &V);
    
    for (int i = 0; i < M; i++) {
        scanf("%d %d", &r, &c);
        
        graph[r][c] = 1;
        graph[c][r] = 1;
    }
    
    dfs(V, N);
    init(N);
    bfs(V, N);
    
    return 0;
}
