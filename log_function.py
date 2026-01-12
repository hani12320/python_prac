def log_args(func):
    def wrapper(*args):
        print("Arguments:",args)
        func(*args)
    return wrapper
@log_args
def add(a, b):
    print("Sum:",a + b)
add(10, 20)
