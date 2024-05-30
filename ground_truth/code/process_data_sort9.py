import ast
def process_line(line: str) -> str:

    key, arrays_str = line.split(':')
    arrays = ast.literal_eval(arrays_str.strip())

    # Modify the inner lists
    for sublist in arrays:
        if sublist[1] == 1:
            sublist[1] = 3

    # Convert the modified arrays back to a string with the key
    modified_line = f"{key}: {arrays}"
    return modified_line


# Input and output file paths
input_file_path = "../data/ground_truth_dd33.txt"
output_file_path = "../data/ground_truth_dd44.txt"


# Open the input file for reading and the output file for writing
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        modified_line = process_line(line)
        output_file.write(modified_line + '\n')



import ast
def process_line(line: str) -> str:

    key, arrays_str = line.split(':')
    arrays = ast.literal_eval(arrays_str.strip())

    # Modify the inner lists
    for sublist in arrays:
        if sublist[1] == 1:
            sublist[1] = 2

    # Convert the modified arrays back to a string with the key
    modified_line = f"{key}: {arrays}"
    return modified_line



input_file_path = "../data/ground_truth_cc33.txt"
output_file_path = "../data/ground_truth_cc44.txt"

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        modified_line = process_line(line)
        output_file.write(modified_line + '\n')
