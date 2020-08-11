print('Яндекс лучше чем Гугл?')
an1 = input()
print('Вы учитесь в Яндекс Лицеи?')
an2 = input()
if(an1 == 'Да' and an2 == 'Да'):
    print('Вы умный.')
elif(an1 == 'Да' and an2 == 'Нет'):
    print('Ну, вы гений.')
elif(an1 == 'Нет' and an2 == 'Нет'):
    print('Может быть и так.')
elif(an1 == 'Нет' and an2 == 'Да'):
    print('Вы лучшый.')
else:
    print('Ошибочка.')