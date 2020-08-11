k = int(input())
i = 0
while (k % 2 == 0):
    k = k / 2
    i += 1
if k == 1:
    print(i)
else:
    print('НЕТ')
