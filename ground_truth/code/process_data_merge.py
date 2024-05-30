def read_file(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(':')
                key = key.strip()
                if value.strip():
                    value = eval(value.strip())
                else:
                    value = []
                data[key] = value
    return data

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

def write_file(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

def main(file1, file2, output_file):
    data1 = read_file(file1)
    data2 = read_file(file2)
    merged_data = merge_dicts(data1, data2)
    write_file(merged_data, output_file)

if __name__ == "__main__":
    file1 = "../data/ground_truth_cd_13.txt"
    file2 = "../data/ground_truth_cc44.txt"
    output_file = "merged_file1.txt"
    main(file1, file2, output_file)

    file1 = "../data/ground_truth_dd44.txt"
    file2 = "../data/ground_truth_cc3.txt"
    output_file = "merged_file2.txt"
    main(file1, file2, output_file)

    file1 = "../data/ground_truth_cd_04.txt"
    file2 = "../data/ground_truth_dd3.txt"
    output_file = "merged_file3.txt"
    main(file1, file2, output_file)

    file1 = "merged_file1.txt"
    file2 = "merged_file2.txt"
    output_file = "merged_file4.txt"
    main(file1, file2, output_file)

    file1 = "merged_file3.txt"
    file2 = "merged_file4.txt"
    output_file = "data_123.txt"
    main(file1, file2, output_file)
