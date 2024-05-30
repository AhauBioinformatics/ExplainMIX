'''Remove the extra parentheses'''

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
input_file = "../data/possible_interpretable_drug1.txt"
output_file = "../data/possible_interpretable_drug11.txt"
remove_last_bracket(input_file, output_file)

input_file = "../data/possible_interpretable_cell1.txt"
output_file = "../data/possible_interpretable_cell11.txt"
remove_last_bracket(input_file, output_file)

''' More than 2,000 data '''
input_file = "../data/possible_interpretable_drug_1.txt"
output_file = "../data/possible_interpretable_drug_11.txt"
remove_last_bracket(input_file, output_file)

input_file = "../data/possible_interpretable_cell_1.txt"
output_file = "../data/possible_interpretable_cell_11.txt"
remove_last_bracket(input_file, output_file)