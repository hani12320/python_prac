def positive_only(func):
    def wrapper(n):
        if n > 0:
            func(n)
        else:
            print("Only positive numbers allowed")
    return wrapper
@positive_only
def square(n):
    print(n*n)
square(5)
square(-3)
