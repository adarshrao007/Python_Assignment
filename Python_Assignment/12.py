def func(value, x,y):
    return {
        'a': lambda x: x+y,
        'b': lambda x: x*y,
        'c': lambda x: x-y,
        'd': lambda x: x/y}.get(value)(x)

# take user input
inp = input('Input a operation Character : ')

print('The result is : ', func(inp, 4, 2))
