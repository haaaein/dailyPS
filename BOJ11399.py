n = int(input())
s = list(map(int, input().split()))

min = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        min += s[j]
print(min)
