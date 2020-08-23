# B. CopyCopyCopyCopyCopy
# by hoanghust

sum_n = 0
testcase_num = int(input())
result = []

while testcase_num > 0:
    n = int(input())
    sum_n += n

    if sum_n > pow(10, 5):
        break

    if (1 <= n) and (n <= pow(10, 5)):
        a = input()
        list_num = a.split()
        for stt, item in enumerate(list_num):
            list_num[stt] = int(item)
            if list_num[stt] < 1 or list_num[stt] > pow(10, 9):
                pass
        out = set(list_num)
        result.append(len(out))
    testcase_num -= 1

for r in result:
    print(r)

