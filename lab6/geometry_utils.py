import math

def circle_area(radius):
    if radius <= 0:
        return None, "Input Error: Radius must be strictly positive."
    return round(math.pi * radius ** 2, 2), None

def circle_perimeter(radius):
    if radius <= 0:
        return None, "Input Error: Radius must be strictly positive."
    return round(2 * math.pi * radius, 2), None

def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        return None, "Input Error: Dimensions must be strictly positive."
    return round(width * height, 2), None

def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        return None, "Input Error: Dimensions must be strictly positive."
    return round(2 * (width + height), 2), None

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return None, "Input Error: Dimensions must be strictly positive."
    return round(0.5 * base * height, 2), None