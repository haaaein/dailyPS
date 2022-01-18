from math import factorial

n = int(input())

count = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    else:
        count += 1

print(count)
