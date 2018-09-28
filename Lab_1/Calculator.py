#Calculator.py


def sum(m, n):
    if n > 0:
        for _ in range(n):
            m += 1
    else:
        for i in range(-n):
            m -= 1
    return m


def divide(m, n):
    # raise exception
    if n == 0:
        raise ZeroDivisionError
    # checks the sign of the operation
    neg = False
    if m < 0:
        neg = not neg
    if n < 0:
        neg = not neg
    m = abs(m)
    n = abs(n)
    times = 0
    while m > 0:
        m -= n
        if m >= 0:
            times += 1
    return -times if neg else times
