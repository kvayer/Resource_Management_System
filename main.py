pizza_menu = ["название 1", "название 2", "название 3"]
choices = []  # Массив для хранения выборов

def make_order():
    while True:
        choice_3 = input("Что Вы хотите?\n1. кофе\n2. пицца\n3. назад\n")
        if choice_3 == "1":
            print("Какое кофе Вы хотите?")
            # Логика выбора кофе
            coffee_choice = input("1. название 1\n2. название 2\n3. название 3\n4. назад\n")
            if coffee_choice == "1":
                print("Вы выбрали название 1 кофе.")
                choices.append("кофе: название 1")  # Сохраняем выбор в массив
                # Дополнительная логика для обработки выбора
                break
            elif coffee_choice == "2":
                print("Вы выбрали название 2 кофе.")
                choices.append("кофе: название 2")  # Сохраняем выбор в массив
                # Дополнительная логика для обработки выбора
                break
            elif coffee_choice == "3":
                print("Вы выбрали название 3 кофе.")
                choices.append("кофе: название 3")  # Сохраняем выбор в массив
                # Дополнительная логика для обработки выбора
                break
            elif coffee_choice == "4":
                continue
            else:
                print("Неверный выбор.")
                continue
        elif choice_3 == "2":
            print("Какую пиццу Вы хотите?")
            # Логика выбора пиццы
            pizza_choice = input("1. название 1\n2. название 2\n3. название 3\n4. назад\n")
            if pizza_choice == "1":
                print("Вы выбрали название 1 пиццу.")
                choices.append("пицца: название 1")  # Сохраняем выбор в массив
                # Дополнительная логика для обработки выбора
                break
            elif pizza_choice == "2":
                print("Вы выбрали название 2 пиццу.")
                choices.append("пицца: название 2")  # Сохраняем выбор в массив
                # Дополнительная логика для обработки выбора
                break
            elif pizza_choice == "3":
                print("Вы выбрали название 3 пиццу.")
                choices.append("пицца: название 3")  # Сохраняем выбор в массив
                # Дополнительная логика для обработки выбора
                break
            elif pizza_choice == "4":
                continue
            else:
                print("Неверный выбор.")
                continue
        elif choice_3 == "3":
            break
        else:
            print("Неверный выбор.")
            continue

while True:
    choice_2 = input("Выберите действие:\n1. сделать заказ\n2. выход\n")
    if choice_2 == "1":
        make_order()
    elif choice_2 == "2":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор.")
        continue

# Вывод всех выборов
print("Все выборы:")
for choice in choices:
    print(choice)
