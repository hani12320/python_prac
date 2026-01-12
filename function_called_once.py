def call_once(func):
    called = False
    def wrapper():
        nonlocal called
        if not called:
            func()
            called = True
        else:
            print("Function already called")
    return wrapper
@call_once
def greet():
    print("Hello!")
greet()
greet()
