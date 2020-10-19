def empty_func(a, b, *, c, d):
    pass


# empty_func(1, 2, 3, 4, c=5, d=6)  # NG
empty_func(1, 2, c=5, d=6)  # OK
