a = input()
b = len(set(a))
if b == 3:
    print('ОК')
elif b == 2:
    print('В числе две одинаковые цифры')
else:
    print('В числе все цифры одинаковые')
