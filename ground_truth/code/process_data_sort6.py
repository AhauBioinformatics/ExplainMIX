def process_line(line):
    array_name, array_content = line.strip().split(": ")
    data = eval(array_content)
    processed_data = [[subarray[0], subarray[2], subarray[1]] for subarray in data]
    return f"{array_name}: {processed_data}\n"

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            processed_line = process_line(line)
            outfile.write(processed_line)



if __name__ == "__main__":
    input_file = "../data/ground_truth_cc22.txt"
    output_file = "../data/ground_truth_cc33.txt"
    main(input_file, output_file)

    input_file = "../data/ground_truth_dd22.txt"
    output_file = "../data/ground_truth_dd33.txt"
    main(input_file, output_file)
