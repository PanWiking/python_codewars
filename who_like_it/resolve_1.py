def first_part(names):
    if len(names) == 0:
        return "no one"
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f'{names[0]} and {names[1]}'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]}'
    else:
        return f'{names[0]}, {names[1]} and {len(names[2:])} others'


def likes(names):
    if len(names) < 2:
        return f'{first_part(names)} likes this'
    return f'{first_part(names)} like this'
