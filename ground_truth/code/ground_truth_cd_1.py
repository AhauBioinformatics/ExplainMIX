import csv
import re

'''
Find interpretable edges centered on predicted cell lines
'''

regex = r"(\d+_[01]_\d+):\[(.*)\]"

with open("../data/possible_interpretable_cell.txt", "r") as infile, \
        open("../data/ground_truth_cd_1.txt", "w", encoding='utf-8') as outfile:
    for line in infile:
        match = re.match(regex, line.strip())

        if match:
            header = match.group(1)

            data = eval('[' + match.group(2) + ']')

            if len(data) == 0:
                outfile.write(line)
                continue
            i = 0
            while i < len(data):
                sublist = data[i]
                a = sublist[0]
                e_match = re.search(r'_(.*?)_', header)
                e = e_match.group(1)

                if int(sublist[2]) == int(e):
                    c = 1
                else:
                    c = 0

                with open('../data/drug_similarity1.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        if str(a) in row and str(header.split('_')[0]) in row:
                            d = float(row[2])

                            if (c == 1 and d > 0.5):
                                pass
                            else:
                                data.pop(i)
                                i -= 1
                                break
                i += 1

            outfile.write(f"{header}: {str(data)}\n")


print("The data is processed and written to a new file.")
