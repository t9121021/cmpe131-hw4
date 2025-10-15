def my_steps(n: int) -> int:

    if not isinstance(n, int) or n < 1 or n > 25:
        raise ValueError("n must be an integer in [1, 25]")
    if n == 1:
        return 1
    a, b = 1, 2 
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b if n > 1 else a
