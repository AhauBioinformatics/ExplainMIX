def reorder_lines(file_with_order, file_to_reorder, output_file):

    with open(file_with_order, 'r', encoding='utf-8') as file:
        order_lines = file.readlines()

    with open(file_to_reorder, 'r', encoding='utf-8') as file:
        reorder_lines = file.readlines()

    reorder_dict = {}
    for line in reorder_lines:
        array_name = line.split(': ')[0]
        reorder_dict[array_name] = line
        
    output_lines = []
    seen_array_names = set()
    for line in order_lines:
        array_name = line.split(': ')[0]
        if array_name in reorder_dict:
            output_lines.append(reorder_dict[array_name])
            seen_array_names.add(array_name)

    for array_name, line in reorder_dict.items():
        if array_name not in seen_array_names:
            output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)

file_with_order = '../data/Sequential_order.txt'

file_to_reorder = '../data/ground_truth_cd_02.txt'
output_file = '../data/ground_truth_cd_03.txt'
reorder_lines(file_with_order, file_to_reorder, output_file)

file_to_reorder = '../data/ground_truth_cd_1.txt'
output_file = '../data/ground_truth_cd_12.txt'
reorder_lines(file_with_order, file_to_reorder, output_file)

file_to_reorder = '../data/ground_truth_cc.txt'
output_file = '../data/ground_truth_cc2.txt'
reorder_lines(file_with_order, file_to_reorder, output_file)

file_to_reorder = '../data/ground_truth_dd.txt'
output_file = '../data/ground_truth_dd2.txt'
reorder_lines(file_with_order, file_to_reorder, output_file)
