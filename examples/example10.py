def outer2(out_param):
    def inner2():
        if out_param == 'TEST':
            return f'Outer def have value: {out_param}'
        else:
            return 'Value not recognized.'
    return inner2

value = outer2('TEST')
print(value())