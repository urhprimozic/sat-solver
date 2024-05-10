# IO oof dimacs format
from cnf import CLAUSE, CNF
from predicate_logic import FORMULA, NEG, VAR


def input_to_literal(n: int):
    """
    Transforms n to VAR(n) and -n to NEG(VAR(-n))
    """
    if n >= 0:
        return VAR(n)
    return NEG(VAR(-n))


def dimacs_input_to_formula():
    """
    Extract formula from dimacs input.

    Returns
    -------
    f : FORMULA
        formula, represented by s
    """
    while True:
        i = input()
        if i[0] == "c":
            continue
        if i[0] == "p":
            i = i.split()
            n_var = int(i[2])
            n_clauses = int(i[3])
            break
    clauses = []
    for i in range(n_clauses):
        c = input()
        c = c.split()
        # remove 0 at the end
        c = c[:-1]
        c = [input_to_literal(int(i)) for i in c]
        clause = CLAUSE(*c)
        clauses.append(clause)
    return CNF(*clauses)


def dimacs_file_to_formula(filename : str):
    """
    Extract formula from dimacs file.

    Parameters
    ----------
    filename : str
        Path to file with dimacs formula
    
    Returns
    -------
    f : FORMULA
        formula, represented by s
    """
    with open(filename, 'r') as f:
        while True:
            i = f.readline()
            if i[0] == "c":
                continue
            if i[0] == "p":
                i = i.split()
                n_var = int(i[2])
                n_clauses = int(i[3])
                break
        clauses = []
        for i in range(n_clauses):
            c = f.readline()
            c = c.split()
            # remove 0 at the end
            c = c[:-1]
            c = [input_to_literal(int(i)) for i in c]
            clause = CLAUSE(*c)
            clauses.append(clause)
    return CNF(*clauses)


def solution_to_dimacs(solution: dict):
    """
    Transforms solution to dimacs format.

    Parameters
    ----------
    solution : dict
        solution dictionary, which maps variables VAR(integer) to True or False

    Returns
    -------
    s : str
        Solution in dimacs format
    """
    if solution is None:
        return 'NO SOLUTION'
    ans = ''
    for var, value in solution.items():
        if value:
            ans += str(var.id) + ' '
        else:
            ans += '-' + str(var.id) + ' '
    return ans[:-1]    

def solution_to_dimacs_file(filename : str, solution : dict):
    '''
    Saves a solution to a file.

    Parameters
    ----------
    filename : str
        Path to file

    solution : dict
        solution dictionary, which maps variables VAR(integer) to True or False
    '''
    ans = solution_to_dimacs(solution)
    with open(filename, 'w') as f:
        f.write(ans)