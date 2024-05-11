# SAT solver
SAT solver, based on dpll algorithm for Logika v računalništvu. Written in python. 

## Usage
All the code is inside the `src` folder. The implementation of the DPLL algorithm is inside `dpll.py`. 
### Read formula from input
To run a SAT solver on a dimacs formula, given in input, run 
`python3 src/main.py` and input the dimacs formula. The solution will be printed in the console. 

### Read formula from file
To run a SAT solver on a dimacs formula, written in a file, run `python3 src/run_on_file.py` and input the filenames of the input file and output file. 

Alternatively, you can run `python3 src/main.py < path_to_input_file > path_to_output_file`.
