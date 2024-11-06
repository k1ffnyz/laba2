import random

# Генерируем список случайных чисел
random_numbers = [random.randint(0, 200) for _ in range(10)]

# Вводим число X
x = int(input("Введите число X: "))

# Используем лямбду для фильтрации чисел, кратных X
multiples_of_x = list(filter(lambda num: num % x == 0, random_numbers))

# Выводим результат
print(f"Случайные числа: {random_numbers}")
print(f"Числа, кратные {x}: {multiples_of_x}")