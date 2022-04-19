data = []
value = 8
# Функция, которая внутри импортирует random
# В цикле генерируется некие 5 пин-кодов (строка из 8-ми цифр)
# Потом преобразовывает все пин-коды, у котрых есть цифра 5 на цифру 6
# И в конце запиывает результат в файл


def solution():
    import random
    for i in range(5):
        result = ''.join(str(random.randint(0, 9)) for _ in range(value))
        print(result)
        data.append(result)
    print(data)
    for index in range(len(data)):
        if '5' in data[index]:
            data[index] = data[index].replace('5', '6')
    with open('test.txt', 'w') as file:
        file.write('\n'.join(data))


if __name__ == '__main__':
    solution()
