def is_year_leap (year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False


check_year = int(input("Введите год для проверки: "))
result = is_year_leap(check_year)
print("год " + str(check_year) + ": " + str(result))