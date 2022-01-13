name = input().rstrip()

count = dict()
for char in name:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

char_front = []
flag = 0
mid = ''
for char in count:
    if count[char] % 2 != 0:  # 문자가 홀수 개수이면
        if flag:
            print("I'm Sorry Hansoo")
            exit()
        else:
            flag = 1
            mid = char
            for _ in range(count[char] // 2):
                char_front.append(char)
    else:
        for _ in range(count[char] // 2):
            char_front.append(char)

char_front.sort()
char_half = ''.join(char_front)
result = char_half + mid + char_half[::-1]
print(result)
