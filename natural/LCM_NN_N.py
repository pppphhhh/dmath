from natural.DIV_NN_N import DIV_NN_N
from natural.GCF_NN_N import GCF_NN_N

def LCM_NN_N(a,b):
    """
    N-14
    НОК двух натуральных чисел
    Копылов Петр, 7305
    """

    # НОК(A, B) = A * B / НОД(A, B)
    return DIV_NN_N(MUL_NN_N(a, b) , GCF_NN_N(a,b))

