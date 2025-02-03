# def circle(radius):
#     circumference = (2 * 3.14 * radius ** 2)
#     area = (3.14 * radius ** 2)
#     print(area, circumference)

# circle(6)

import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius ** 2
    return area, circumference

a, c = circle_stats(3)
print("Area: ",math.ceil(a))
print("Circumference: ",math.ceil(c))