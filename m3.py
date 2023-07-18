import threading

def print_cube(num):
    """

    Вычисляет куб от заданного числа num

    :param num:
    :return:
    """
    print(f'Куб {num} -> {num * num * num}')


def print_square(num):
    """

    Вычисляет куб от заданного числа num

    :param num:
    :return:
    """
    print(f'Квадрат {num} -> {num ** 2}')

if __name__ == '__main__':
    threading1 = threading.Thread(target=print_square, args=(10,))
    threading2 = threading.Thread(target=print_cube, args=(10,))
    threading1.start()
    threading2.start()
    threading1.join()
    threading2.join()
