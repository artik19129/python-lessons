str = float(input())
if abs(str) < abs(0.000001):
    print(1000000.0)
else:
    print(str ** -1)
