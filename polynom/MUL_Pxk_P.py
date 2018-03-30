from common import copy_P, rat_to_Q


def MUL_Pxk_P(polynom, k):
    """
    P-4
    Умножение многочлена на x^k
    Мартыненко Александр, 7305
    """
    # Копируем полином
    result = copy_P(polynom)
    # Степень многочлена увеличиваем на k
    result[0] += k
    # Добавляем k нулевых коэффициентов в массив коэффициентов
    result[1] = [rat_to_Q(0, 1)] * k + result[1]
    # Возвращаем полученный многочлен
    return result

