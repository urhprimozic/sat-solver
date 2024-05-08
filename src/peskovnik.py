from cnf import *
import dpll

v1 = VAR(1)
nv1 = NEG(VAR(1))
v2 = VAR(2)
nv2 = NEG(VAR(2))

c1 = CLAUSE(v1, v2, nv1)
c2 = CLAUSE(v2, v1)
c3 = CLAUSE(v2)

f1 = CNF(c1, c2, c3)
