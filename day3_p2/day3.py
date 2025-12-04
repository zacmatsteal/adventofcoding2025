import re

INPUT_PATH = "input\\input.txt"
OUTPUT_PATH = "output\\output.txt"

NB_DIGITS = 12

def main():
    matrix = parse_input()
    solution = solve(matrix)

    print("The solution is: " + str(solution))
    store_output(solution)

def parse_input():
    matrix = list()

    try:
        with open(INPUT_PATH) as input:
            for line in input:
                matrix.append(line.rstrip('\n')) # Removes the \n at the end of each line
        return matrix
    except:
        raise Exception("Error in the parsing of the input")

def store_output(output):
    try:
        with open(OUTPUT_PATH, "w") as file:
            file.write(str(output))
    except:
        raise Exception("Error when trying to store the output")
        
def solve(matrix: list[str]):
    solution = 0
            
    for line in matrix:
        joltage = int(solve_line(line, initValues(NB_DIGITS), "0"))
        solution += joltage

    return solution

# Recursively solves one line
def solve_line(line: str, values: list[str], solution):
    # Case where every character in the line has been checked already
    if len(line) == 0:
        return solution + values[0]

    # Case where some of the first digits are part of the final solution
    while len(line) < len(values):
        solution += values[0]
        values = values[1:]

    # Case where there is one better digit to pick
    for i in range(len(values)):
        if int(values[i]) < int(line[0]):
            for j in range(i, len(values)):
                values[j] = "0"
            values[i] = line[0]
            return solve_line(line[1:], values, solution)

    # Case where there is no better digit to pick
    return solve_line(line[1:], values, solution)

def initValues(nbValues: int):
    values_init = list()
    
    for i in range(NB_DIGITS):
        values_init.append("0")

    return values_init
    
if __name__=="__main__":
    main()
