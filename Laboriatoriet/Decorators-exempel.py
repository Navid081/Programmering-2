def my_decorator(func):
    def wrapper():
        print("Running (func.__name__)")
        func()
        print("Complete")
    return wrapper
        

@my_decorator
def do_this():
    print("Doing this")

def do_that():
    print("Doing that")


do_this()
print("-----")
