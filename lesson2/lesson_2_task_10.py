def bank(x, y):
    for i in range(y):
        x = x * 1.1
        x = round(x, 2)
    return x


x = int(input("Размер вклада: "))
y = int(input("Срок вклада: "))
print(bank(x, y))