def extract_lines(input_file, output_file1, output_file2):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file1, 'w') as f1, open(output_file2, 'w') as f2:
        for i in range(0, len(lines), 4):
            f1.write(f"{lines[i].strip()}{lines[i + 1].strip()}\n")
            f2.write(f"{lines[i].strip()}{lines[i + 2].strip()}\n")

''' More than 20,000 data '''
input_file = "../data/possible_interpretable_cd1.txt"
output_file1 = "../data/possible_interpretable_drug.txt"
output_file2 = "../data/possible_interpretable_cell.txt"

extract_lines(input_file, output_file1, output_file2)

''' More than 2,000 data '''
input_file = "../data/possible_interpretable_cd_.txt"
output_file1 = "../data/possible_interpretable_drug_.txt"
output_file2 = "../data/possible_interpretable_cell_.txt"

extract_lines(input_file, output_file1, output_file2)

''' Processing data that does not conform to the format '''

def remove_last_bracket(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:

        if line.endswith(']\n'):
            modified_lines.append(line[:-2] + '\n')
        else:
            modified_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

''' More than 20,000 data '''
input_file = "../data/possible_interpretable_drug.txt"
output_file = "../data/possible_interpretable_drug1.txt"
remove_last_bracket(input_file, output_file)

input_file = "../data/possible_interpretable_cell.txt"
output_file = "../data/possible_interpretable_cell1.txt"
remove_last_bracket(input_file, output_file)

''' More than 2,000 data '''
input_file = "../data/possible_interpretable_drug_.txt"
output_file = "../data/possible_interpretable_drug_1.txt"
remove_last_bracket(input_file, output_file)

input_file = "../data/possible_interpretable_cell_.txt"
output_file = "../data/possible_interpretable_cell_1.txt"
remove_last_bracket(input_file, output_file)