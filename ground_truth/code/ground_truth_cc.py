import csv
import re

'''
Get an explanation of the true cell line connection edge
'''

regex = r"(\d+_[01]_\d+):\[(.*)\]"

with open("../data/possible_interpretable_cc.txt", "r") as file:
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
            print(item)
            c = item[1]

            with open("../data/drug_cellLine_relation.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:

                    if str(a) in row and str(c) in row:

                        d = row[2]
                        if b == d:
                            new_data.append(item)
                        break

        new_line = f"{a}_{b}_{m}: {new_data}\n"
        with open("../data/ground_truth_cc.txt", "a") as new_file:
            new_file.write(new_line)

