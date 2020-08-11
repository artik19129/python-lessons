password = input()
password2 = input()
a = 0
while a == 0:
    if len(password) < 8:
        print("Короткий!")
        password = input()
        password2 = input()
    elif "123" in password:
        print("Простой!")
        password = input()
        password2 = input()
    elif password != password:
        print("Различаются.")
        password = input()
        password2 = input()
    else:
        print("OK")
        a += 2
