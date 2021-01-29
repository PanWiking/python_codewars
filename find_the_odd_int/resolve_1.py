def find_it(seq):
    seq_sorted = sorted(seq)
    flag = 0
    hold = None
    for item in seq_sorted:
        if hold != item and hold is not None:
            if flag % 2:
                return hold
            else:
                flag = 1
        else:
            flag += 1
        hold = item
    return hold
