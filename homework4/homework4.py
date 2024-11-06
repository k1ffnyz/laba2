from datetime import date

def calculate_age():
    # Запрашиваем ввод даты рождения
    while True:
        try:
            birth_date = input("Введите вашу дату рождения в формате ДД/ММ/ГГГГ: ")
            day, month, year = map(int, birth_date.split('/'))
            birthdate = date(year, month, day)
            break
        except ValueError:
            print("Неверный формат ввода. Пожалуйста, введите дату в формате ДД/ММ/ГГГГ.")
    
    # Получаем текущую дату
    today = date.today()
    
    # Вычисляем возраст
    age = today.year - birthdate.year
    
    # Учитываем месяц и день
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
        
    return age

# Вызов функции
age = calculate_age()
print(f"Ваш возраст: {age}")