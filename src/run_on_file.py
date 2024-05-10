from dimacs import dimacs_file_to_formula, solution_to_dimacs_file
from dpll import dpll

in_file = input('Please enter a filename of a file with input: ')
out_file = input('Please enter a filename of a file to which the output should be written: ')
f = dimacs_file_to_formula(in_file)
solution = dpll(f)
solution_to_dimacs_file(out_file, solution)
print(solution)

