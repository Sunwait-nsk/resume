import math


class Circle:

    def __init__(self, name):
        self.name = name
        self.coordinate_X = 0
        self.coordinate_Y = 0
        self.radius = 1

    def square(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def increase(self, count):
        self.radius *= count

    def info(self):
        print('Круг {} имеет центр в точке ({}, {}) и радиус {}'.format(
            self.name, self.coordinate_X, self.coordinate_Y, self.radius))


class Shapes:

    def __init__(self, count):

        self.shapes = [Circle(number) for number in range(1, count + 1)]


def intersection_shape(shape_1, shape_2):
    distance = math.sqrt((shape_1.coordinate_X - shape_2.coordinate_X) ** 2 + (
            shape_1.coordinate_Y - shape_2.coordinate_Y) ** 2)
    if abs(shape_1.radius - shape_2.radius) <= distance <= (shape_1.radius + shape_2.radius):
        print('Круги пересекаются')
    else:
        print('Круги не пересекаются')


circles = Shapes(2)
circles.shapes[0].coordinate_X += 3
circles.shapes[0].coordinate_Y += 2
circles.shapes[0].radius = 2
square = circles.shapes[0].square()
perimeter = circles.shapes[0].perimeter()
circles.shapes[0].info()
print('Круг под номером {} имеет S = {}, P = {}'.format(circles.shapes[0].name, square, perimeter))
circles.shapes[1].coordinate_X = 6
circles.shapes[1].coordinate_Y = 3
circles.shapes[1].radius = 3
circles.shapes[1].info()
intersection_shape(circles.shapes[0], circles.shapes[1])
print('********')
circles.shapes[0].coordinate_X = 1
circles.shapes[0].coordinate_Y = 1
circles.shapes[0].radius = 1
circles.shapes[0].info()
intersection_shape(circles.shapes[0], circles.shapes[1])


