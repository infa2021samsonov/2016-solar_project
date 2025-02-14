# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # FIXME: do the same for planet
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                    print("Bruh")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    arr = line.split()
    if arr[0] == "Star":
        star.R = int(arr[1])
        star.color = arr[2]
        star.m = float(arr[3])
        star.x = float(arr[4])
        star.y = float(arr[5])
        star.Vx = float(arr[6])
        star.Vy = float(arr[7])
    else:
        print("It`s not a star.")

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    arr = line.split()
    if arr[0] == "Planet":
        planet.R = int(arr[1])
        planet.color = arr[2]
        planet.m = float(arr[3])
        planet.x = float(arr[4])
        planet.y = float(arr[5])
        planet.Vx = float(arr[6])
        planet.Vy = float(arr[7])
    else:
        print("It`s not a planet.")


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        for obj in space_objects:
            if obj.type == 'planet' or 'star':
                print(obj.type, 'Radius:', obj.R, 'Color:', obj.color, 'Mass:', obj.m, 'x:', obj.x, 'y:', obj.y, 'Vx:', obj.Vx, 'Vy:', obj.Vy, file=out_file)
# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
