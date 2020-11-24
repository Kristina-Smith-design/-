def Stephorse(x1,y1,x2,y2):
    if type(x1) not in [int]:
        raise TypeError("x1 must be non-negative real number only")
    if type(y1) not in [int]:
        raise TypeError("y1 must be non-negative real number only")
    if type(x2) not in [int]:
        raise TypeError("x2 must be non-negative real number only")
    if type(y2) not in [int]:
        raise TypeError("y2 must be non-negative real number only")

    if x1 < 0:
        raise ValueError("x1 can't be negative")
    if y1 < 0:
        raise ValueError("y1 can't be negative")
    if x2 < 0:
        raise ValueError("x2 can't be negative")
    if y2 < 0:
        raise ValueError("y2 can't be negative")

    if x1 > 8:
        raise ValueError("x1 can't be > 8")
    if y1 > 8:
        raise ValueError("y1 can't be > 8")
    if x2 > 8:
        raise ValueError("x2 can't be > 8")
    if y2 > 8:
        raise ValueError("y2 can't be > 8")

    if x1 == 0:
        raise ValueError("x1 can't be 0")
    if y1 == 0:
        raise ValueError("y1 can't be 0")
    if x2 == 0:
        raise ValueError("x2 can't be 0")
    if y2 == 0:
        raise ValueError("y2 can't be 0")

    if abs(abs(x1 - x2)-abs(y1 - y2)) == 1:
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
            return 'Step'
        elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
            return 'Step'
        else:
            return 'Stop'
    else:
        return 'Stop'