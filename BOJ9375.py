testCase = int(input())

for _ in range(testCase):
    dic = {}
    num = int(input())
    for i in range(num):
        v, k = input().split()
        if k not in dic:
            dic[k] = 1
        else:
            dic[k] += 1

    ans = 1
    for value in dic.values():
        ans *= (value + 1)
    print(ans - 1)
