n, m = map(int, input().split())

no_heard = []
no_seen = []

for _ in range(n):
    name = input()
    no_heard.append(name)

for _ in range(m):
    name = input()
    no_seen.append(name)

result = list(set(no_heard) & set(no_seen))

print(len(result))
result.sort()

for i in result:
    print(i)
