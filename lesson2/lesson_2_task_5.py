def month_to_season(n):
    if (n == 1 and n == 2 or n == 12):
        return "Зима"
    elif (n >= 3 and n <= 5):
        return "Весна"
    elif (n >= 6 and n <= 8):
        return "Лето"
    elif (n >= 9 and n <= 11):
        return "Осень"
    else:
        return "Такого месяца не существует"

print(month_to_season(int(input("Введите номер месяца: "))))