def month_to_season(n):
    if (n != 0 and n <= 2 or n == 12):
        print("Зима")
    elif (n > 2 and n < 6):
        print("Весна")
    elif (n > 5 and n < 9):
        print("Лето")
    elif (n >= 10 and n < 12):
        print("Осень")
    else:
        print("Такого месяца не существует")

month_to_season(0)