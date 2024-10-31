import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()

    def fight(self):
        enemies = 100
        counter = 0
        while enemies > 0:
            if self.power > 0:
                enemies -= self.power
                counter += 1
                if enemies > 0:
                    print(f'{self.name} сражается {counter} дней(дня)..., осталось {enemies} воинов.')

            time.sleep(1)

        if enemies <= 0:
            print(f'{self.name} одержал победу спустя {counter} дней(дня)!\n')



if __name__ == '__main__':
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    # Вывод строки об окончании сражения

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print('Все битвы закончились!')