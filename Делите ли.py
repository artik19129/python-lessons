flag = False
num = int(input())
otvet = 0
cout = num
while otvet != num:
    if num // cout == num / cout:
        if num // cout != 0:
            otvet = num // cout
            print(otvet, end=' ')
    cout = cout - 1
if num == 1:
    print()
    print('���')
elif num == 2:
    print()
    print('�������')
elif num % 2 == 0:
    print()
    print('�������')
else:
    print()
    print('���')