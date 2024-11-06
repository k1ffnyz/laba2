def outer(outer_parameter1, outer_parameter2):
    def inner(inner_parameter1, inner_parameter2):
        return inner_parameter1 + inner_parameter2
    return inner(outer_parameter1, outer_parameter2)

print(outer(9, 10))