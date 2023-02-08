# функция сортировки пузырьковым методом
def sort_bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# функция бинарного поиска левого и правого элементов
def bin_search(array, numbers_user, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == numbers_user:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif numbers_user < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return bin_search(array, numbers_user, left, middle - 1)
    else:  # иначе в правой
        return bin_search(array, numbers_user, middle + 1, right)


# тело программы
# ввод чисел, проверка верности данных, сортировка

while True:
    try:
        array = input(
            "Введите последовательность чисел через пробел: ").split()  # разделение по разделителю (пробел)

        array_mod = [int(x) for x in array]  # Запись строки целых чисел

        sort_bubble(array_mod)  # сортировка
        print("после сортировки методом пузырек: ", array_mod)

        user_number = input("Введите число для определения индекса: ")
        user_number = int(user_number)

        break

    except ValueError:
        print(f"Ошибка {ValueError}")
        print("Введено недопустимое значение!")
        answer = input("Повторить ввод чисел? (+ / -): ")
        if answer != '+':
            print("До свидания")
            exit(1)
        else:
            print("В следующий раз будьте внимательнее!")

# проверка на наличие искомого числа в списке
if user_number not in array_mod:
    print(f"Числа {user_number} нет среди чисел последовательности. {array_mod}")
    if user_number < min(array_mod):
        print(f"число {user_number} меньше минимального последовательности. {min(array_mod)}")
    if user_number > max(array_mod):
        print(f"число {user_number} больше максимального последовательности {max(array_mod)}")
    exit(1)

# вызов функции бинарного поиска левого и правого элементов
number_index = bin_search(array_mod, user_number, 0, len(array_mod) - 1)

# определение места искомого числа в списке
print("Индекс введенного числа в списке: ", number_index + 1)
# анализ числа в списке
if number_index == 0:
    print(f"число {user_number} первое значение в списке, следующее {array_mod[number_index + 1]}")
elif number_index == int(len(array_mod) - 1):
    print(f"число {user_number} последнее значение в списке, предыдущее значение {array_mod[number_index - 1]}")
else:
    print(f"предыдущее значение {array_mod[number_index - 1]}, следующее {array_mod[number_index + 1]}")
