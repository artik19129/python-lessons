a = input()
b = 0
MIN = 190
MAX = 150

while a != '!':
    a = int(a)
    if a >= 150 and a <= 190:
        b += 1
        if a >= MAX:
            MAX = a
        if a <= MIN:
            MIN = a
    a = input()
print(b)
print(MIN, MAX)
