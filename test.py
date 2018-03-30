from polynom import MUL_Pxk_P
import common

P = common.coef_to_P([ (1, 1), (2, 1), (3, 1) ])
result = MUL_Pxk_P(P, 4)
result = common.P_to_coef(result)
for c in result:
    print(c)
