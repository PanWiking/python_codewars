def validate_pin(pin):
    if pin.isdecimal():
        if len(pin) == 6 or len(pin) == 4:
            try:
                if int(pin) >= 0:
                    return True
                else:
                    return False
            except Exception as e:
                return False
        else:
            return False
    return False
