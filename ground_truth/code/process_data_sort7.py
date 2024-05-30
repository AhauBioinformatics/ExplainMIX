with open("../data/ground_truth_cd_12.txt", "r") as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    parts = line.split(":")
    prefix = parts[0]
    array_str = parts[1].strip()
    array = eval(array_str)

    processed_array = [[subarray[0], subarray[2], subarray[3]] for subarray in array]

    processed_line = f"{prefix}: {processed_array}\n"
    processed_lines.append(processed_line)

with open("../data/ground_truth_cd_13.txt", "w") as file:
    file.writelines(processed_lines)


##############
# with open("../data/ground_truth_cd_03.txt", "r") as file:
with open("../data/ground_truth_cd_03.txt", "r") as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    parts = line.split(":")
    prefix = parts[0]
    array_str = parts[1].strip()
    array = eval(array_str)

    processed_array = [[subarray[0], subarray[2], subarray[3]] for subarray in array]

    processed_line = f"{prefix}: {processed_array}\n"
    processed_lines.append(processed_line)

with open("../data/ground_truth_cd_04.txt", "w") as file:
    file.writelines(processed_lines)

#########

with open("../data/ground_truth_dd2.txt", "r") as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    parts = line.split(":")
    prefix = parts[0]
    array_str = parts[1].strip()
    array = eval(array_str)

    processed_array = [[subarray[0], subarray[2], subarray[3]] for subarray in array]

    processed_line = f"{prefix}: {processed_array}\n"
    processed_lines.append(processed_line)

with open("../data/ground_truth_dd3.txt", "w") as file:
    file.writelines(processed_lines)

###############
with open("../data/ground_truth_cc2.txt", "r") as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    parts = line.split(":")
    prefix = parts[0]
    array_str = parts[1].strip()
    array = eval(array_str)

    processed_array = [[subarray[0], subarray[2], subarray[3]] for subarray in array]

    processed_line = f"{prefix}: {processed_array}\n"
    processed_lines.append(processed_line)

with open("../data/ground_truth_cc3.txt", "w") as file:
    file.writelines(processed_lines)
