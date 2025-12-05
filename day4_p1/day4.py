INPUT_PATH = "input\\input.txt"
OUTPUT_PATH = "output\\output.txt"

PAPER_CHAR = '@'

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

        line_len = len(matrix[0])
        for line in matrix:
            if len(line) != line_len:
                raise Exception("The length of each line of the map must be the same")
        return matrix
    except:
        raise Exception("Error in the parsing of the input")

def store_output(output):
    try:
        with open(OUTPUT_PATH, "w") as file:
            file.write(str(output))
    except:
        raise Exception("Error when trying to store the output")


def solve(paperMap: list[str]):
    heatmap = createHeatmap(paperMap)
    return countPapersAccessible(paperMap, heatmap)

def countPapersAccessible(paperMap: list(), heatmap: list()):
    solution = 0

    for line in range(len(heatmap)):
        for col in range(len(heatmap)):
            if heatmap[line][col] < 4 and paperMap[line][col] == PAPER_CHAR:
                solution += 1
    
    return solution

def createHeatmap(paperMap: list[str]):
    heatmap = createZeroMap(len(paperMap), len(paperMap[0]))

    for line in range(len(heatmap)):
        for col in range(len(heatmap)):
            if paperMap[line][col] == PAPER_CHAR:
                heatmap = createPaperImpact(heatmap, line, col)

    return heatmap

def createPaperImpact(heatmap: list(), line: int, col:int):
    isMaxLeft = col == 0
    isMaxRight = col == len(heatmap[0]) - 1
    isMaxTop = line == 0
    isMaxBottom = line == len(heatmap) - 1

    if (not isMaxLeft):
        heatmap[line][col-1] += 1
        
    if (not isMaxRight):
        heatmap[line][col+1] += 1
        
    if (not isMaxTop):
        heatmap[line-1][col] += 1
        if (not isMaxLeft):
            heatmap[line-1][col-1] += 1
        if (not isMaxRight):
            heatmap[line-1][col+1] += 1
            
    if (not isMaxBottom):
        heatmap[line+1][col] += 1
        if (not isMaxLeft):
            heatmap[line+1][col-1] += 1
        if (not isMaxRight):
            heatmap[line+1][col+1] += 1

    return heatmap

def createZeroMap(lines: int, cols: int):
    zeroMap = list()

    for _ in range(lines):
        line = []
        
        for _ in range(cols):
            line.append(0)

        zeroMap.append(line)

    return zeroMap

if __name__=="__main__":
    main()
