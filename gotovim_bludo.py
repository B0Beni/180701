import asyncio
import os
import time
from datetime import datetime

def dish(num, prepare, wait):
    """

    :param num: номер блюда по порядку
    :param prepare: время на подготовку
    :param wait: ожидание готовности
    :return:
    """
    print(f'Подготовка к приготовлению блюда {num} - {datetime.now().strftime("%H:%S")}. Приготовление {prepare} минут')
    time.sleep(prepare)
    print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%S")}. Ожидание {num} {wait} блюда')
    await asyncio.sleep(wait)
    print(f'В {datetime.now().strftime("%H:%S")}. блюдо {num} готово')

async def gotovim_bludo():
    tasks = [
    asyncio.create_task(dish(1, 2, 3)),
    asyncio.create_task(dish(2, 5, 10)),
    asyncio.create_task(dish(3, 3, 5))
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time.time()  # время начало работы
    if os.name ==
    delta = int(time.time() - t0)  # затраченное время
    print(f'В {datetime.now().strftime("%H:%S")} все готово')
    print(f'Затрачено времени - {delta}')

