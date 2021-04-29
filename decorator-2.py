def outer(message):
    print('In the outer function')

    def inner():
        print('Clling the inner function')
        print(message)


    return inner

f = outer('Hello world ')
f()


#### Decorator

def decorator(original_func):
    print('In the decorator function\n')

    def wrapper():
        print(f'wrapper executed before {original_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return original_func()

    return wrapper


@decorator
def print_something():
    print('print_something is being ran!')

print_something()

### Using decorator in one way
#decorated_f = decorator(print_something)
#decorated_f()





#### using decorator in different way

def decorator2(original_func):
    print('In the decorator2 function\n')

    def wrapper(*args, **kwargs):
        print(f'wrapper executed before {original_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return original_func(*args, **kwargs)

    return wrapper


@decorator2
def print_something_more(arg1, arg2):
    print(f'printing argument_1 = {arg1} and argument_2 = {arg2}')


print_something_more(1, 2)


