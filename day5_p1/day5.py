import re

INPUT_PATH = "input\\input.txt"
OUTPUT_PATH = "output\\output.txt"

id_ranges = list()
ids_products = []
solution = 0

def main():
    parse_input()
    solve()
    
    print("The solution is: " + str(solution))
    store_output(solution)
    
def parse_input():
    parse_products()
    parse_ranges()

def parse_products():
    try:
        with open(INPUT_PATH) as ids_raw:
            # Flags that gets set to true once we get to the empty line that separates
            # the id ranges from the ids of the products that we need to check
            isAfterRanges = False
            for line in ids_raw:
                if isAfterRanges:
                    ids_products.append(int(line))
                else:
                    isAfterRanges = not '-' in line
    except:
        raise Exception("Error in the parsing of the input (products)")

def parse_ranges():
    try:
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
    except:
        raise Exception("Error in the parsing of the input (ranges)")

def store_output(output):
    try:
        with open(OUTPUT_PATH, "w") as file:
            file.write(str(output))
    except:
        raise Exception("Error when trying to store the output")

def solve():
    global solution
    
    for product in ids_products:
        if (isFresh(product)):
            solution += 1

def isFresh(id: int):
    for id_range in id_ranges:
        if id >= id_range[0] and id <= id_range[1]:
            return True
    return False

if __name__=="__main__":
    main()
