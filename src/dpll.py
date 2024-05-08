from cnf import CNF, CLAUSE
from predicate_logic import NEG

# code for dpll alrogithm is adapted from https://en.wikipedia.org/wiki/DPLL_algorithm
def dpll(f : CNF):
    
    '''
    DPLL algorithm

    INPUT
    ----------
    f - formula in CNF form!. Of type dicmacs    '''
    # unit propagation:
    while True:
        unit_literal = f.find_unit_literal()
        if unit_literal is None:
            break
        f.unit_propagate(unit_literal)

    # pure literal elimination:
    while True:
        pure_literal = f.find_pure_literal()
        if pure_literal is None:
            break
        f.pure_literal_assign(pure_literal)
    # stopping conditions:
    if f.is_empty():
        return True 
    if f.has_empty_clause() is not None:
        return False
    
    # DPLL procedure:
    literal = f.choose_literal()
    return dpll( CNF( *f.clauses, CLAUSE(literal)) ) or dpll(CNF( *f.clauses, CLAUSE(NEG(literal))))
   