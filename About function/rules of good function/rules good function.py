# Функция, которая внутри импортирует random
# В цикле генерируется некие 5 пин-кодов (строка из 8-ми цифр)
# Потом преобразовывает все пин-коды, у котрых есть цифра 5 на цифру 6
# И в конце запиывает результат в файл


import random
# ХОРОШАЯ ФУНКЦИЯ:
# 1. Имеет читаемое название, нужную информацию получает в аргументах
# 2. Короткая (10-15 строк)/ читаемая
# 3. Возвращает результат (NO PRINT!)
# 4. Независима (NO GLOBAL!!!), и не меняет ничего вне себя
# 5. Умеет делать что-то одно, но умеет это хорошо и знает всё для этого
# 6. Если меняет пришедший аргумент, то возвращает None
# 7. Тестируема!


def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))   # Функция генерации пин-кода


def replace_fives(a_list: list, value: str) -> list[str]:
    return [element.replace('5', value) for element in a_list]  # Функция преобразования пин-кода


def replace_fives_inplace(a_list: list, value: str):
    for index in range(len(a_list)):
        a_list[index] = a_list[index].replace('5', value)    # Изменение приходящего списка, обязательно возвращать None


def write_file(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]   # Этой строчкой мы делаем список из 5-ти пинов
    replace_fives_inplace(pins, '6')         # Изменяем цифры 5 на 6
    str_list = '\n'.join(pins)        # Преобразовываем в строку то, что мы получили
    print(pins)
    write_file('test1.txt', str_list)  # Записываем полученное в файл с передачей строки
