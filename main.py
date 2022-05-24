import eel
import random


def main():  # старт приложения
    eel.init("web")

    eel.start("index.html", size=(1600, 900))


@eel.expose  # анотация(передаем ф-ю на JS код
def generate_data(b1, b2, x1, x2, x3, a3, zk, vk, d1, d2):
    step = 200  # кол-во точек между двумя днями
    x1 /= 10000  # округление до 4 знаков после запятой нач усл
    x2 /= 10000
    x3 /= 10000
    res1 = []  # массив точек для кажого графика
    res2 = []
    res3 = []
    for i in range(10 * step):
        res1.append([i / step, round(x1 * 10000)])  # точка по времени вторая колво особей
        res2.append([i / step, round(x2 * 10000)])
        res3.append([i / step, round(x3 * 10000)])
        dx1 = x1 * (-b1 * x2 + x3 * zk - d1) / step
        dx2 = x2 * (b2 * x1 - x3 * vk - d2) / step
        dx3 = x3 * (-zk * x1 - vk * x2 + a3) / step
        x1 += dx1
        x2 += dx2
        x3 += dx3
        if x1 <= 0:
            x1 = 0
        if x2 <= 0:
            x2 = 0
        if x3 <= 0:
            x3 = 0
        x1 = round(x1, 4)  # окргуление до 4х знаков полсе запятой
        x2 = round(x2, 4)
        x3 = round(x3, 4)
        if x1 <= 0:
            x1 = 0
        if x2 <= 0:
            x2 = 0
        if x3 <= 0:
            x3 = 0


    return [res1, res2, res3]


if __name__ == '__main__':  # вход в нашу программу
    main()
