from natural import LCM_NN_N, GCF_NN_N TRANS_N_Z
from integer import ABS_Z_N, TRANS_Z_N, DIV_ZZ_Z MULL_ZZ_Z
def FAC_P_Q(polynom):
    """
    P-7
    Вынесение ищ многочлена НОК знаменателей коэффициентов
    и НОД числителей
    Ким Артём, 7305
    """
    #TODO
    nd=(1,1);nk=(1,1);
     for i in range (polynom[0]+1):
        a=polynom[1][i][0]
        b=polynom[1][i][1]
        ABS_Z_N(a)
        nd=GCF_NN_N(nd,a)
        nk=LCM_NN_N(nk,b)

    TRANS_N_Z(nk)
    TRANS_N_Z(nd)
    for j in range (polynom[0]+1):
       #Здесь мб криво
       polynom[i][j][0]=DIV_ZZ_Z(polynom[i][j][0],nd)

       a=polynom[i][j][1]
       TRANS_N_Z(a)
       b=DIV_ZZ_Z(nk,a)
       polynom[i][j][0]=MUL_ZZ_Z(polynom[i][j][0],b)
       i=j+1
         
    return [[0,nd[0],nd[1]],[nk]]

