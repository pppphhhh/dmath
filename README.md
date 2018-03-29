## Внутренние структуры

Натуральное число представляет из себя пару (n, A), где n - количество разрядов в числе, A - массив цифр размера n.
Цифры в массиве хранятся в обратном порядке, например 123 представляется как (3, [3, 2, 1]).

Целое - тройка (b, n, A), где n и A - то же, что для натурального, b - знак числа (0 - положительное, 1 - 
отрицательное).

Рациональное - пара (n, m), где n - целое (числитель), m - натуральное (знаменатель)

Многочлен - пара (n, C), где n - степень многочлена, С - массив рациональных чисел (коеффициенты) в обратном порядке,
например многочлен x^2 + 2x + 5 будет иметь массив коэффициентов, эквивалентный [5, 2, 1] (числа будут рациональными)
