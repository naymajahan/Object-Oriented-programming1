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

        return original_func() + 'extra string!'
    return wrapper


