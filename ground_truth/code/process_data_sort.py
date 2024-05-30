'''
Sort and cull data
'''

def filter_and_order_arrays(file_with_order, file_to_filter, output_file):
    with open(file_with_order, 'r', encoding='utf-8') as file:
        order_lines = file.readlines()

    with open(file_to_filter, 'r', encoding='utf-8') as file:
        filter_lines = file.readlines()

    filter_dict = {}
    for line in filter_lines:
        array_name = line.split(': ')[0]
        filter_dict[array_name] = line

    output_lines = []
    for line in order_lines:
        array_name = line.split(': ')[0]
        if array_name in filter_dict:
            output_lines.append(filter_dict[array_name])

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)

''' Based on cell lines '''
file_with_order = '../data/Sequential_order.txt'
file_to_filter = '../data/ground_truth_cd_1.txt'
output_file = '../data/ground_truth_cd_12.txt'

filter_and_order_arrays(file_with_order, file_to_filter, output_file)

''' Based on drug '''
file_with_order = '../data/Sequential_order.txt'
file_to_filter = '../data/ground_truth_cd_0.txt'
output_file = '../data/ground_truth_cd_02.txt'

filter_and_order_arrays(file_with_order, file_to_filter, output_file)
