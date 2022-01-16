from sys import stdin
li = list(map(int, stdin.readline().split()))

a = li[0]
b = li[1]

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
