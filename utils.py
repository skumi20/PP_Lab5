"""
Moduł utils dostarcza podstawowe operacje arytmetyczne.
"""

def add(a: int, b: int) -> int:
    """
    Zwraca sumę dwóch liczb całkowitych.

    :param a: pierwsza liczba całkowita
    :param b: druga liczba całkowita
    :return: suma a i b
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Zwraca różnicę między dwoma liczbami całkowitymi.

    :param a: pierwsza liczba całkowita
    :param b: druga liczba całkowita
    :return: wartość a minus b
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Zwraca iloczyn dwóch liczb całkowitych.

    :param a: pierwsza liczba całkowita
    :param b: druga liczba całkowita
    :return: iloczyn a i b
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Dzieli pierwszą liczbę całkowitą przez drugą.

    :param a: dzielna (całkowita)
    :param b: dzielnik (całkowity)
    :return: wynik dzielenia jako wartość zmiennoprzecinkowa
    :raises ZeroDivisionError: jeśli b == 0
    """
    return a / b
