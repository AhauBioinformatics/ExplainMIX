def extract_arrays(input_file):
    with open(input_file, 'r') as file:
        arrays = [eval(line.strip()) for line in file]

    result = []

    # Iterate over each array in the input
    for array in arrays:
        two_dimensional_array = [[array], []]  # Initialize the 2D array with two empty arrays
        start_value = array[0]
        end_value = array[-1]

        # Find arrays containing the start value
        for other_array in arrays:
            if start_value in other_array and other_array != array and other_array not in two_dimensional_array[0]:
                two_dimensional_array[0].append(other_array)
                start_value = other_array[0]

        # Find arrays containing the end value
        for other_array in arrays:
            if end_value in other_array and other_array != array and other_array not in two_dimensional_array[1]:
                two_dimensional_array[1].append(other_array)
                end_value = other_array[-1]

        result.append(two_dimensional_array)

    return result


def write_result(output_file, result):
    with open(output_file, 'w') as file:
        for two_dimensional_array in result:
            start_value = two_dimensional_array[0][0][0]
            sensitive = two_dimensional_array[0][0][-2]
            end_value = two_dimensional_array[0][0][-1]
            array_name = f"{start_value}_{sensitive}_{end_value}"
            file.write(f'{array_name}:\n')
            for array_list in two_dimensional_array:
                # Convert array_list to the desired format [ [], [] ]
                formatted_array_list = "[" + ', '.join(map(str, array_list)) + "]"
                file.write(f'{formatted_array_list}\n')
            file.write('\n')

input_file = "../data/drug_cellLine_relation_.txt"
output_file = "../data/possible_interpretable_cd_.txt"


result = extract_arrays(input_file)
write_result(output_file, result)
