from predicate_logic import *
from itertools import chain


def is_literal(f: FORMULA):
    if isinstance(f, VAR):
        return True
    if isinstance(f, NEG):
        if isinstance(f.f, VAR):
            return True
    return False


def is_negation(f: FORMULA):
    if isinstance(f, NEG):
        return True
    return False


class CLAUSE(FORMULA):
    """
    Disjunction of finitly many literals
    """

    def __init__(self, *literals) -> None:
        if False in map(is_literal, literals):
            raise TypeError("Not a literal!")
        self.literals = list(literals)

    def find_unit_literal(self):
        """
        Returns a unit literal l if a clouse only contains l , None otherwise
        """
        if len(self.literals) == 1:
            return self.literals[0]
        return None

    def unit_propagate(self, unit_literal):
        # if literal (which is set to TRUE) is included in this clause, the clause is TRUE --> remove it
        # else  if NEG(literal) is included --> remove  all NEG(literal)
        # else do not remove
        if unit_literal in self.literals:
            return True  # aka remove the clause
        # remove NEG(literal)s
        self.literals = [l for l in self.literals if l != NEG(unit_literal)]

    def find_pure_literal():
        raise NotImplementedError

    def pure_literal_assign(pure_literal):
        raise NotImplementedError

    def is_empty():
        raise NotImplementedError

    def find_empty_clause():
        raise NotImplementedError

    def __str__(self) -> str:
        ans = "("
        for l in self.literals:
            ans += str(l)
            ans += " or "
        ans = ans[:-4]
        ans += ")"
        return ans

    def __repr__(self) -> str:
        return str(self)


is_clause = lambda x: isinstance(x, CLAUSE)


class CNF(FORMULA):
    """
    Conjunction of finitly many clauses
    """

    def __init__(self, *clauses) -> None:
        if False in map(is_clause, clauses):
            raise TypeError("Not a clause!")
        self.clauses = list(clauses)

    def find_unit_literal(self):
        """
        Returns the first unit clause
        """
        for c in self.clauses:
            l = c.find_unit_literal()
            if l is not None:
                return l
        return None

    def unit_propagate(self, unit_literal):
        # pythonic magic --> first propagates all the clauses, than removes the True ones
        self.clauses = [
            c for c in self.clauses if c.unit_propagate(unit_literal) is None
        ]

    def find_pure_literal(self):
        # list of all different literals
        literals = list(set(chain(*[c.literals for c in self.clauses])))
        # literals are either:
        # TYPE 1: NEG(VAR(x)) or
        # TYPE 2: VAR((x))

        # encode variable_id : type. If both types appear, type = 0
        var_types = {}
        for l in literals:
            if isinstance(l, NEG):
                var_id = l.f.id
                l_type = 1
            else:
                var_id = l.id
                l_type = 2
            if var_types.get(var_id) is None:
                var_types[var_id] = l_type
            else:
                if var_types[var_id] != l_type and var_types[var_id] != 0:
                    # both types --> not a pure literal
                    var_types[var_id] = 0

        for val_id, l_type in var_types.items():
            if l_type == 1:
                # just negations
                return NEG(VAR(val_id))
            if l_type == 2:
                # just variables
                return VAR(val_id)
        # else no pure variables found
        return None

    def pure_literal_assign(self, pure_literal):
        # removes all the clauses that include the pure literal
        self.clauses = [c for c in self.clauses if not (pure_literal in c.literals)]

    def is_empty(self):
        if len(self.clauses) == 0:
            return True
        return False

    def has_empty_clause(self):
        for c in self.clauses:
            if len(c.literels) == 0:
                return True
        return False

    def __str__(self) -> str:
        ans = ""
        for c in self.clauses:
            ans += str(c)
            ans += " & "
        ans = ans[:-3]
        ans += ""
        return ans

    def __repr__(self) -> str:
        return str(self)
