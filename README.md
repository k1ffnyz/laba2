# laba2
## example1
```
Код определяет функцию _example_, 
которая выводит фразу "Hello, World!!!! (c) Kazantsev", 
и затем вызывает эту функцию.
```

## example2
```
Код определяет функцию _example_, которая всегда возвращает 
True, затем проверяет это значение: если оно истинно, 
выводит сообщение "Значение истинно.", иначе — "Значение ложно."; 
наконец, выводит само значение.
```

## example3
```
Функция _identify_product_by_name_ проверяет название продукта: 
если это "авокадо", возвращает "Это фрукт"; если "чай" — "Это напиток"; 
в остальных случаях — "Неизвестный продукт". Программа классифицирует 
авокадо как фрукт и выводит результат.
```

## example4
```
Код проверяет, установлено ли значение 
переменной _example_ как None, и в зависимости 
от этого выводит сообщение "Пусто" 
или "Есть что-то".
```

## example5
```
Функция _питомец_ создаёт словарь с информацией 
о домашнем животном на основе переданных имени, 
породы и возраста, а затем программа 
использует эту функцию для создания 
профиля кота Барсика.
```

## example6
```

Функция _собака_ создаёт словарь с информацией 
о собаке на основе переданных клички, окраса и возраста, 
а затем программа использует эту 
функцию для создания профиля 
щенка Шарика, которого 
потом выводит на экран.
```

## example7
```
Функция _example_args_ принимает любое количество
 позиционных аргументов, собирает их в кортеж 
 и выводит его, а программа вызывает эту 
 функцию с несколькими аргументами 
 для демонстрации работы.
```

## example8
```
Функция _outer_ принимает два параметра, определяет вложенную функцию _inner_, которая суммирует два внутренних параметра и возвращает результат, а затем вызывает _inner_ с внешними параметрами, возвращая сумму 19.
```

## example9
```
Функция _outer_ принимает строку, передает её во вложенную функцию _inner_, которая проверяет длину строки и возвращает разные сообщения в зависимости от результата.
```

## example10
```
Функция _outer2_ принимает строку, создаёт и возвращает вложенную функцию _inner2_, которая проверяет значение строки и возвращает разные сообщения в зависимости от результата, а затем программа вызывает эту функцию с результатом проверки на соответствие строке 'TEST'.
```

## example11
```
Программа определяет список книг, функцию для изменения регистра и добавления метки о прочтении, а затем применяет эту функцию к каждому элементу списка, меняя регистр и добавляя метку о прочтении или непрочтении в зависимости от начала названия книги с буквы 'P'.
```

## example12
```

Функция _my_generate_ генерирует числа в заданном диапазоне, пропуская те, которые не делятся на 3, а затем выводит их, изменяя начальную точку и шаг для нового диапазона от 1 до 12, начиная с шага 1.
```

## homework4
```
Функция _calculate_age_ запрашивает дату рождения, проверяет корректность ввода, вычисляет возраст на основе текущей даты, учитывая корректировку на основе месяцев и дней, и возвращает полный возраст.
```

## homework5
```
Программа генерирует список случайных чисел от 0 до 200, запрашивает число X, фильтрует числа, кратные X с помощью лямбда-выражения, и выводит результаты: сгенерированный список чисел и список чисел, кратных X.
```

## homework6
```
Функция _get_odd_numbers_ возвращает нечетные числа из диапазона от 0 до 29. Программа запрашивает первый, пятый и последний элементы списка, фильтруя их с помощью счетчика и оператора _if_, и выводит их.
```

## game
```
Код описывает классическую игру "Камень, Ножницы, Бумага". В программе определяются правила игры, где пользователь выбирает один из трех вариантов: "Камень", "Ножницы" или "Бумага", а компьютер случайным образом выбирает свой ход. Игрок вводит свой выбор, а компьютер реагирует на него. Если выбор пользователя совпадает с выбором компьютера, объявляется ничья. Если пользователь выигрывает, программа сообщает об этом, а если проигрывает, выводит соответствующее сообщение.
```