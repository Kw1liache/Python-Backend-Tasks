def add_numbers(a: float, b: float) -> float:
    """Складывает два числа.

    Args:
        a (float): Первое слагаемое.
        b (float): Второе слагаемое.

    Returns:
        float: Сумма двух чисел.
    """
    return a + b

def divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    return a / b