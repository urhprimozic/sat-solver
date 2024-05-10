from dimacs import dimacs_input_to_formula, solution_to_dimacs
from dpll import dpll

print('Please enter a formula in dimacs format:')
f = dimacs_input_to_formula()
solution = dpll(f)
print(solution_to_dimacs(solution))

