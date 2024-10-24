# mymath에서 필요한 함수들 불러오기
from mymath import *

# 삼각형의 넓이 계산
base = 3
height = 10
print("삼각형의 넓이:", triangle_area(base, height))

# 원의 넓이 계산
radius = 4
print("원의 넓이:", circle_area(radius))

# 직육면체의 넓이 계산
length = 5
width = 10
height = 4
print("직육면체의 넓이:", cuboid_area(length, width, height))
