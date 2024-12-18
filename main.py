def compute_area(r):
    pi = 3.14159
    return r * r * pi

def find_max(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def multiply_and_add(a, b, c):
    result = a * b
    return result + c

def main():
    print('Area:', compute_area(5))
    print('Max:', find_max(3, 9, 6))
    print('Result:', multiply_and_add(2, 3, 4))