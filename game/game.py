import random

def play_game():
    choices = ["Камень", "Ножницы", "Бумага"]
    
    user_choice = input("Ваш выбор (Камень, Ножницы, Бумага): ").title()
    
    if user_choice not in choices:
        print("Ошибка: неверный ввод. Попробуйте еще раз.")
        return
    
    computer_choice = random.choice(choices)
    
    print(f"Компьютер выбрал: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
         (user_choice == "Ножницы" and computer_choice == "Бумага") or \
         (user_choice == "Бумага" and computer_choice == "Камень"):
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")

if __name__ == "__main__":
    play_game()