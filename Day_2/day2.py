import re

INPUT_PATH = "input\\input.txt"
RESULT_PATH = "output\\output.txt"

id_list = list()

def main():
    parse_input()
    result = solve(id_list)

    print("The solution is: " + str(result))
    store_output(result)
    

# Parse the input to get a list of tuples
def parse_input():
    try:
        with open(INPUT_PATH) as ids:
            ids_string = ids.read()
            ids_left = re.findall("(\d+)-\d+", ids_string)
            ids_right = re.findall("\d+-(\d+)", ids_string)
            for i in range(len(ids_left)):
                range_left = int(ids_left[i])
                range_right = int(ids_right[i])
                if range_left > range_right:
                    raise Exception("The id on the left of the range cannot be greater than the id on the right")
                id_list.append((range_left, range_right))

    except:
        raise Exception("Error when parsing the input file")

def store_output(solution: int):
    try:
        with open(RESULT_PATH, "w") as file:
            file.write(str(solution))
    except:
        raise Exception("Error when storing the solution")

def solve(id_list: list()):
    result = 0
    
    for id_tuple in id_list:
        for id in range(id_tuple[0], id_tuple[1] + 1):
            if is_invalid(id):
                result += id

    return result

def is_invalid(id: int):
    id_str = str(id)
    
    if len(id_str) % 2 == 1:
        return False;

    return is_duplicated(id_str)

def is_duplicated(id: str):
    left = id[:(len(id)//2)]
    right = id[(len(id)//2):]
    
    return left == right
    
    

if __name__=="__main__":
    main()
