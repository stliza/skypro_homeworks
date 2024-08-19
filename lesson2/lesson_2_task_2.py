def is_year_leap (year):
    if (year % 4 == 0):
        return True
    else:
        return False

check_year = 2011
result = is_year_leap(check_year)
print("год " + str(check_year) + ": " + str(result))