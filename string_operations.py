user_input = input("Введіть рядок з 15 символів: ")

if len(user_input) == 0:
    print("Рядок пустий. Програма завершує роботу.")

else:
    while len(user_input) < 15:
        user_input += user_input * 3

    user_list = list(user_input)
    print("Повний список:", user_list, sep="\n")
    print("Останні 5 елементів:", user_list[-5:], sep="\n")
    print("Список у зворотній послідовності:", user_list[::-1], sep="\n")
    print("Список з парними індексами:", user_list[::2], sep="\n")
    user_list[:5] = user_list[-5:]
    print("Список з однаковими 5 елементами на початку та наприкінці:", user_list, sep="\n")
