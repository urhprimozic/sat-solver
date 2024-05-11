from cnf import CNF, CLAUSE, is_literal
from predicate_logic import NEG, FORMULA


def solve_literal(l: FORMULA):
    """
    Returns a solution of a literal

    Parameters
    ----------
    l : CNF
        formula to solve. Must be a literal (either VAR(*) or NEG(VAR(*)))

    Returns
    ------
    solution : dict
        A dictionary, containing one entry, which maps the variable in the literal to a solution of l.
    """
    if is_literal(l):
        if isinstance(l, NEG):
            return {l.f: False}
        return {l: True}
    raise TypeError("Literal expected!  (either VAR(*) or NEG(VAR(*))")


# code for dpll alrogithm is adapted from the psdeudocode, found in  https://en.wikipedia.org/wiki/DPLL_algorithm (10.5.2024)
def dpll(f: CNF):
    """
    DPLL algorithm


    Parameters
    ----------
    f : CNF
        formula in CNF form

    Returns
    -------
    - solution : dict
        Dictionary mapping variables to either `True` or `False` in such way that the mapping of `f` is true

    or
    - `None` if `f` is not satisfiable


    """

    def algorithm(f: CNF, solution: dict):
        # unit propagation:
        while True:
            unit_literal = f.find_unit_literal()
            if unit_literal is None:

                break

            # this literal should be true. Add this to the solutions
            solution.update(solve_literal(unit_literal))
            # remove clauses with unit_literal, remove NEG(unit_literal) from clauses
            f.unit_propagate(unit_literal)

        # pure literal elimination:
        while True:
            pure_literal = f.find_pure_literal()
            if pure_literal is None:

                break
            # set the literal to true
            solution.update(solve_literal(pure_literal))
            # remove all the clauses with pure_literal
            f.pure_literal_assign(pure_literal)

        # stopping conditions:
        if f.is_empty():
            return solution
        if f.has_empty_clause():
            return None

        # DPLL procedure:
        literal = f.choose_literal()

        #create a copy of a formula:
        f1 = CNF(*f.clauses, CLAUSE(NEG(literal))).copy()

        # if setting literal to True solves the formula, thats it. Otherwise try with NEG(literal)
        ans = algorithm(CNF(*f.clauses, CLAUSE(literal)), solution)
        if ans is not None:
            return ans
        return algorithm(f1, solution)

    return algorithm(f, {})
