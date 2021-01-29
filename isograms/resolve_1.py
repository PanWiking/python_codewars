def is_isogram(string):
    if len(set(string.lower())) == len(string):
        return True
    else:
        return False
