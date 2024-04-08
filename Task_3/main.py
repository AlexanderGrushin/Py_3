# Для набора точек на плоскости найти такие три точки, для которых периметр
# треугольника с вершинами в данных точках будет минимальным. В случае существования
# нескольких подходящих троек точек – выбрать произвольную.

import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def find_minimum_perimeter(points):
    min_perimeter = float('inf')
    min_points = []

    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                side1 = distance(points[i], points[j])
                side2 = distance(points[j], points[k])
                side3 = distance(points[k], points[i])

                perimeter = side1 + side2 + side3

                if perimeter < min_perimeter:
                    min_perimeter = perimeter
                    min_points = [points[i], points[j], points[k]]

    return min_points


# Чтение точек из файла
points = []
with open('points.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split())
        points.append((x, y))

# Поиск трех точек с минимальным периметром
result_points = find_minimum_perimeter(points)

# Вывод результата
print("Точки с минимальным периметром:")
for point in result_points:
    print(point)
