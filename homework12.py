def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params()
print_params(5, 6, False)
print_params('test')

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [11, 'hello', False]
values_dict = {'a': 7, 'b': 'string', 'c': [4, 5]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, True]
print_params(*values_list_2, 42)