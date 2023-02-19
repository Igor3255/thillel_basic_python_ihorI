import math


def degrees2radians(degrees):
    return degrees * 3.14159265359 / 180


cos60 = math.cos(degrees2radians(60))
cos45 = math.cos(degrees2radians(45))
cos40 = math.cos(degrees2radians(40))

print(f"cos(60) = {cos60}")
print(f"cos(45) = {cos45}")
print(f"cos(40) = {cos40}")
