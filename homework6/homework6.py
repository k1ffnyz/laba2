def get_odd_numbers():
    """Генератор, возвращающий нечетные числа из диапазона range(30)"""
    for number in range(30):
        if number % 2 != 0:
            yield number

# Получение первого, пятого и последнего значений
first_value = next(get_odd_numbers())
fifth_value = None
last_value = None

counter = 1
for value in get_odd_numbers():
    if counter == 5:
        fifth_value = value
    last_value = value
    counter += 1

# Вывод результатов
print(f"Первое значение: {first_value}")
print(f"Пятое значение: {fifth_value}")
print(f"Последнее значение: {last_value}")