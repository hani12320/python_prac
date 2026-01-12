def division_by_zero(func):
    def wrapper(a, b):
        if b == 0:
            print("Division by zero not allowed")
        else:
            func(a, b)
    return wrapper
@division_by_zero
def divide(a, b):
    print("Result:", a / b)
divide(10,2)
divide(10,0)
