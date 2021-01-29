def sum_digits(n):
    return sum([int(item) for item in list(str(n))])


def digital_root(n):
    output = sum_digits(n)
    while len(str(output)) != 1:
        output = sum_digits(output)
    return output
