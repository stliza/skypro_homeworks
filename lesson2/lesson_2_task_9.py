var_1 = 37
var_2 = 99
print("Задано:", var_1)
print("Задано:", var_2)

# Первый вариант
var_1, var_2 = var_2, var_1
print("Поменяли 1:", var_1)
print("Поменяли 1:", var_2)

# Второй вариант (возвращаем к первоначальному виду)
buf = var_1
var_1 = var_2
var_2 = buf
print("Поменяли 2:", var_1)
print("Поменяли 2:", var_2)