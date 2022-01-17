#include <stdio.h>

typedef long long int ll;

int N;
ll M;
int tree[1001000];

ll cutting(int m)
{
    ll ret;

    ret = 0;
    for (int i = 0; i < N; i++)
        if (tree[i] > m) ret += (tree[i] - m);

    return ret;
}

int main(void)
{
    int left, right, mid, ans;

    scanf("%d %lld", &N, &M);

    for (int i = 0; i < N; i++) scanf("%d", &tree[i]);

    left = 0;
    right = 1000000000;
    ans = -1;
    while (left <= right)
    {
        mid = (left + right) / 2;

        if (cutting(mid) < M)
            right = mid - 1;
        else
            ans = mid;
            left = mid + 1;
    }

    printf("%d\n", ans);
    
    return 0;
}
