from cnf import *
from dpll import dpll
from predicate_logic import *

v1 = VAR(1)
nv1 = NEG(VAR(1))
v2 = VAR(2)
nv2 = NEG(VAR(2))

c1 = CLAUSE(v1, v2, nv1)
c2 = CLAUSE(v2, v1)
c3 = CLAUSE(v2)
c4 = CLAUSE(VAR(3), NEG(VAR(2)), VAR(4))
c5 = CLAUSE(NEG(VAR(4)), VAR(1))


f1 = CNF(c1, c2, c3)
f2 = CNF( c4, c5, c1  )