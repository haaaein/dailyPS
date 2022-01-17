import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:  # 이분 탐색
    mid = (start + end) // 2

    total = 0
    for t in tree:
        if t >= mid:
            total += t - mid  # 나무를 자르고 가져갈 수 있는 총 길이
            # print(total, mid, end)

    if total >= M:  # 가져갈 수 있는 총 나무 길이가 M보다 같거나 많을 시
        start = mid + 1  # 더 길게 나무를 잘라야 하므로 start = mid + 1

    else:  # 가져갈 수 있는 총 나무 길이가 M보다 작다면
        end = mid - 1  # 더 짧게 나무를 잘라야 하므로 end = mid -1

print(end)
