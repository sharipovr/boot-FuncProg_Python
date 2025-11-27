def args_logger(*args, **kwargs):
    for index, a in enumerate(args, start=1):
        print(f"{index}. {a}")

    kwargs_sorted = sorted(kwargs.items())
    for ka in kwargs_sorted:
        print(f"* {ka[0]}: {ka[1]}")