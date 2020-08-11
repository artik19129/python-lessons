a = input()
b = input()
if(a == 'да' and b == 'нет'):
    print('ВЕРНО')
elif(a == 'нет' and b == 'да'):
    print('ВЕРНО')
elif(a == 'да' and b == 'да'):
    print('ВЕРНО')
elif(a == 'нет' and b == 'нет'):
    print('ВЕРНО')    
else:
    print('НЕВЕРНО')