from cnf import CNF

# code for dpll alrogithm is adapted from https://en.wikipedia.org/wiki/DPLL_algorithm
def dpll(f : CNF):
    
    '''
    DPLL algorithm

    INPUT
    ----------
    f - formula in CNF form!. Of type dicmacs    '''
    # unit propagation:
    while True:
        unit_clause = f.find_unit_clause()
        if unit_clause is None:
            break
        f.unit_propagate(unit_clause)

    # pure literal elimination:
    while True:
        pure_literal = f.find_pure_literal()
        if pure_literal is None:
            break
        f.pure_literal_assign(pure_literal)
    # stopping conditions:
    if f.is_empty():
        return True 
    if f.find_empty_clause() is not None:
        return False
    
    # DPLL procedure:
    literal = f.choose_literal()
    return dpll(CONJ(f, literal)) or dpll(CONJ(f, NEG(literal)))
   