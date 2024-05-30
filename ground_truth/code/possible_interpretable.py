def remove_first_array_from_lines(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            if (i + 1) % 4 == 2:  # Check if it's a 4n+2 line
                # Split the line into individual arrays
                arrays = line.strip().split('], [')
                # Remove the first array from the list
                arrays = arrays[1:]
                # Join the remaining arrays back into a single line
                new_line = '[[' + '], ['.join(arrays) + ']\n'
                output_file.write(new_line)
            else:
                output_file.write(line)

def extract_arrays(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        arrays = [eval(line.strip()) for line in file]

    result = []

    for array in arrays:
        two_dimensional_array = [[array], []]
        start_value = array[0]
        end_value = array[-1]

        for other_array in arrays:
            if start_value in other_array and other_array != array and other_array not in two_dimensional_array[0]:
                two_dimensional_array[0].append(other_array)
                start_value = other_array[0]

        for other_array in arrays:
            if end_value in other_array and other_array != array and other_array not in two_dimensional_array[1]:
                two_dimensional_array[1].append(other_array)
                end_value = other_array[-1]

        result.append(two_dimensional_array)

    return result

def write_result(output_file, result):
    with open(output_file, 'w', encoding='utf-8') as file:
        for two_dimensional_array in result:
            start_value = two_dimensional_array[0][0][0]
            sensitive = two_dimensional_array[0][0][-2]
            end_value = two_dimensional_array[0][0][-1]
            array_name = f"{start_value}_{sensitive}_{end_value}"
            file.write(f'{array_name}:\n')
            for array_list in two_dimensional_array:
                formatted_array_list = "[" + ', '.join(['[' + ', '.join(map(str, elem)) + ']' for elem in array_list]) + "]"
                file.write(f'{formatted_array_list}\n')
            file.write('\n')

input_file = "../data/drug_cellLine_relation.csv"
output_file = "../data/possible_interpretable_cd.txt"

result = extract_arrays(input_file)
write_result(output_file, result)
#remove_first_array_from_lines('possible_interpretable_cd.txt', 'possible_interpretable_cd1.txt')
