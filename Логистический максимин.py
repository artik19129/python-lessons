number = int(input())
maximum = 0
road = 1
for element in range(number):
    tunnel = int(input())
    m = 100000000
    for element_2 in range(tunnel):
        height = int(input())
        if m > height:
            m = height
    if maximum < m:
        maximum = m
        road = element + 1
print(road, maximum)