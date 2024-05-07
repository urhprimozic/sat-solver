from predicate_logic import * 

def is_literal(f : FORMULA):
    if isinstance(f, VAR):
        return True
    if isinstance(f, NEG):
        if isinstance(f.f , VAR):
            return True
    return False

class CLAUSE(FORMULA):
    '''
    Disjunction of finitly many literals
    '''
    def __init__(self, *literals) -> None:
        if False in map(is_literal, literals):
            raise TypeError('Not a literal!')
        self.literals = literals


is_clause = lambda x : isinstance(x, CLAUSE)
class CNF(FORMULA):
    '''
    Conjunction of finitly many clauses
    '''
    def __init__(self, *clauses) -> None:
        if False in map(is_clause, clauses):
            raise TypeError('Not a clause!')
        self.clauses = clauses