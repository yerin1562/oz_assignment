import math

# 삼각형 넓이
def triangle_area(base, height):
    return 0.5 * base * height

# 원의 넓이
def circle_area(radius):
    return math.pi * radius ** 2

# 직육면체의 넓이
def cuboid_area(length, width, height):
    return 2 * (length * width + width * height + height * length)
