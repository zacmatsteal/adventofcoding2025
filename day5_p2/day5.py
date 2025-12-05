import re

INPUT_PATH = "input\\input.txt"
OUTPUT_PATH = "output\\output.txt"


def main():
    id_ranges = parse_input()
    
    solution = solve(id_ranges)
    
    print("The solution is: " + str(solution))
    store_output(solution)
    
def parse_input():
    try:
        id_ranges = list()
        with open(INPUT_PATH) as ids_raw:
            ids = ids_raw.read()
            
            ids_left = re.findall("(\d+)-", ids)
            ids_right = re.findall("-(\d+)", ids)

            for i in range(len(ids_left)):
                range_left = int(ids_left[i])
                range_right = int(ids_right[i])
                if range_left > range_right:
                    raise Exception("The lower bounds need to be lower than the higher bounds")
                id_ranges.append((range_left, range_right))
        return id_ranges
    except:
        raise Exception("Error in the parsing of the input (ranges)")

def store_output(output):
    try:
        with open(OUTPUT_PATH, "w") as file:
            file.write(str(output))
    except:
        raise Exception("Error when trying to store the output")

def solve(id_ranges: list()):
    ranges_cleaned = cleanRangeList(id_ranges)
    return countFresh(ranges_cleaned)

# Takes a list of tuples that represent ranges: (min, max) and removes redundancy
def cleanRangeList(ranges: list()):
    # Orders the list of tuples in ascending order
    ranges.sort(key = lambda x: x[0])

    i = 0
    
    while i < (len(ranges) - 1):
        if ranges[i][1] >= ranges[i+1][0]:
            range_min = ranges[i][0]
            range_max = max(ranges[i][1], ranges[i+1][1])
            ranges[i] = (range_min, range_max)
            del ranges[i + 1]
        else:
            i += 1

    return ranges

def countFresh(ranges: list()):
    solution = 0

    for i in range(len(ranges)):
        solution += ranges[i][1] - ranges[i][0] + 1

    return solution

if __name__=="__main__":
    main()
