def log_decorator(func):
    def wrapper(*args, **kwargs):
        if args or kwargs:
            raise TypeError(f"La fonction '{func.__name__}' ne doit prendre aucun argument.")
        else:
            print("Hey")
            func()
            print("bye")

    return wrapper
 
@log_decorator
def function_test():
    print(f"Cette fonction ne prend pas d'arguments.")

function_test()
function_test("df")

