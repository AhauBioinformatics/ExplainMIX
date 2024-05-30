import csv
import re


regex = r"(\d+_[01]_\d+):\[(.*)\]"

with open("../data/possible_interpretable_dd.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    match = re.match(regex, line)
    if match:
        a = match.group(1).split("_")[0]
        b = match.group(1).split("_")[1]
        m = match.group(1).split("_")[2]
        data = eval(match.group(2))

        new_data = []
        for item in data:
            if isinstance(item, (list, tuple)) and len(item) > 1:
                c = item[1]

                with open("../data/drug_cellLine_relation.csv", "r") as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if str(m) in row and str(c) in row:
                            d = row[2]
                            if b == d:
                                new_data.append(item)
                            break

        new_line = f"{a}_{b}_{m}: {new_data}\n"
        with open("../data/ground_truth_dd.txt", "a") as new_file:
            new_file.write(new_line)
