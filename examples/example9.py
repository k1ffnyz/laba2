def outer(out_param):
    def inner(in_param):
        if len(in_param) > 0:
            return f'Inner function received non-empty value: {in_param}'
        else:
            return 'Inner function received an empty value'
    return inner(out_param)

print(outer('VALUE'))