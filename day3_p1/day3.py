INPUT_PATH = "input\\input.txt"
OUTPUT_PATH = "output\\output.txt"

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
                matrix.append(line[:len(line)-1]) # Removes the \n at the end of each line
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
        joltage = int(solve_line(line, "0", "0"))
        solution += joltage

    return solution

# Recursively solves one line
def solve_line(line: str, first: str, second: str):
    # Base case where the line is at its last character
    if len(line) <= 1:
        return first + str(max(int(second), int(line[0])))
    # Case where there are still characters to check
    if int(first) < int(line[0]):
        return solve_line(line[1:], line[0], "0")
    elif int(second) < int(line[0]):
        return solve_line(line[1:], first, line[0])
    else:
        return solve_line(line[1:], first, second)

if __name__=="__main__":
    main()
