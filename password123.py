password = input()
apassword = input()

if len(password) < 8:
    print('Короткий!')
elif apassword != password:
    print('Различаются.')
else:
    print('OK')
