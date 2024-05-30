import pandas as pd
import numpy as np

'''ground_truth cell line-cell line'''
def clean_row(row):
    row = row.strip().strip('[').strip(']').split(',')
    return [float(val.strip()) for val in row]

data_lines = []
with open("../data/drug_cellLine_relation_.txt", "r") as file:
    for line in file:
        cleaned_line = clean_row(line)
        data_lines.append(cleaned_line)

we_pred_data = np.array(data_lines)

relation_data = pd.read_csv("../data/cellLine_similarity1.csv", header=None)


arrays_dict = {}
m = 0

for row in we_pred_data:
    a, b, c = int(row[0]), int(row[2]), int(row[3])
    array_name = f"{a}_{b}_{c}"
    m = m + 1
    arrays_dict[array_name] = []

    for _, rel_row in relation_data[(relation_data[0] == c) & (relation_data[2] == 1)].iterrows():
        arrays_dict[array_name].append(rel_row.tolist())


with open("../data/possible_interpretable_cc.txt", "w") as f:
    for key, val in arrays_dict.items():
        f.write(f"{key}:{val}\n")


'''ground_truth drug-drug'''
relation_data = pd.read_csv("../data/drug_similarity1.csv", header=None)
arrays_dict = {}
m = 0

for row in we_pred_data:
    a, b, c = int(row[0]), int(row[2]), int(row[3])
    array_name = f"{a}_{b}_{c}"
    m = m + 1
    arrays_dict[array_name] = []

    for _, rel_row in relation_data[(relation_data[0] == c) & (relation_data[2] == 1)].iterrows():
        arrays_dict[array_name].append(rel_row.tolist())


with open("../data/possible_interpretable_dd.txt", "w") as f:
    for key, val in arrays_dict.items():
        f.write(f"{key}:{val}\n")