import sys
nums = []
for line in sys.stdin:
    if int(line.strip()) == 0:
        break
    nums.append((line.strip()))

total = 1
for num in nums:
    for n in num:
        if int(n) == 1:
            total += 2
        elif int(n) == 0:
            total += 4
        else:
            total += 3
        total += 1
    print(total)
    total = 1
