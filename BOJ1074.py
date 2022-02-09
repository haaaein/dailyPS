n, r, c = map(int, input().split())
answer = 0


def solution(n, x, y):
    global answer
    if x == r and y == c:
        print(int(answer))
        exit(0)
    if n == 1:
        answer += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        answer += n ** 2
        return
    solution(n / 2, x, y)
    solution(n / 2, x, y + n / 2)
    solution(n / 2, x + n / 2, y)
    solution(n / 2, x + n / 2, y + n / 2)


solution(2 ** n, 0, 0)
