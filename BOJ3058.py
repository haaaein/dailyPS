from sys import stdin
num = list(map(int, stdin.readline().split()))

sum = 0
for _ in range(num[0]):
    li = list(map(int, stdin.readline().split()))
    even = []
    for i in range(len(li)):
        if li[i] % 2 == 0:
            sum += li[i]
            even.append(li[i])
    print(str(sum) + " " + str(min(even)))
    sum = 0
