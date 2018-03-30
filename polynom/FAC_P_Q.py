from natural import LCM_NN_N, GCF_NN_N
frfrom integer import ABS_Z_N, TRANS_Z_N, DIV_ZZ_Z
dedef FAC_P_Q(polynom):
    """
    P-7
    Вынесение ищ многочлена НОК знаменателей коэффициентов
    и НОД числителей
    Ким Артём, 7305
    """
    #TODO
    nd=(1,1);nk=(1,1);
     for i in range (polynom[0]+1):
        a=polynom[1[i[0]]]
        b=polynom[1[i[1]]]
        TRANS_Z_N(a)
        nd=GCF_NN_N(nd,a)
        nk=LCM_NN_N(nk,b)
        
    for j in range (polynom[0]+1):
        polynom[1[i[0]]]=DIV_ZZ_Z(polynom[1[i[0]]],[0,nd[0],nd[1]])#Здесь мб криво
        polynom[1[i[1]]]=DIV_ZZ_Z(polynom[1[i[1]]],[0,nk[0],hk[1]])#
        i=i+1
         
    return polynom
