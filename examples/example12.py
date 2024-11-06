def my_generate(start=0, stop=5, step=1):
    number = start
    while number <= stop:
        if number % 3 == 0:  # новое условие: проверка делимости на 3
            yield number
        number += step

ranger = my_generate(1, 12)  # новый диапазон от 1 до 12
for value in ranger:
    print(value)